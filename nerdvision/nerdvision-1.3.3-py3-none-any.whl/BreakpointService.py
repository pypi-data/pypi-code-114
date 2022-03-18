import copy
import logging
import os
import random
import sys
import threading
import time
from collections import deque

from nerdvision import settings
from nerdvision.ErrorHandler import ErrorHandler
from nerdvision.FrameProcessor import FrameProcessor
from nerdvision.ProfilerService import ProfilerService
from nerdvision.Utils import Utils
from nerdvision.models.Breakpoint import Breakpoint, BreakpointConfig
from nerdvision.models.EventSnapshot import Watcher

our_logger = logging.getLogger("nerdvision")


class BreakpointService(object):

    def __init__(self, client_config, set_trace=True, context_service=None):
        self.client_config = client_config
        self.breakpoints = {}
        self.var_id = 1
        self.context_service = context_service
        self.rate_limit_tracker = {}
        self.callbacks = {}
        self.old_settrace = sys.gettrace()
        self.old_threading = threading._trace_hook
        if set_trace:
            sys.settrace(self.trace_call)
            threading.settrace(self.trace_call)

    def shut_down(self):
        # We need to reset these to what they where before we changed them, else tests get screwy
        sys.settrace(self.old_settrace)
        threading.settrace(self.old_threading)

    def trace_call(self, frame, event, arg):
        # todo: do we need to call the old trace function?
        if len(self.breakpoints) == 0:
            return None

        lineno = frame.f_lineno
        filename = frame.f_code.co_filename

        breakpoints_for = self.breakpoints_for(filename)

        if settings.is_point_cut_debug_enabled():
            our_logger.debug("Found %s breakpoints for %s", len(breakpoints_for), filename)

        if event == "call" and len(breakpoints_for) == 0:
            return None

        current_thread = threading.current_thread()

        if event in ["line", "return", "exception"] and current_thread.ident in self.callbacks:
            self.process_callbacks(frame, event, arg, current_thread)

        if event == "line":
            line_start = int(round(time.time() * 1000))
            # Make copy to ensure that the rate limit info isn't cleared while processing
            rate_limit_copy = copy.deepcopy(self.rate_limit_tracker)
            bps_types = self.find_match(breakpoints_for, lineno, frame, rate_limit_copy)

            if bps_types['count'] > 0:
                tracepoints = bps_types['tps']
                config = BreakpointConfig(tracepoints)

                processor = FrameProcessor(config, client_config=self.client_config)

                skipped = None

                # If we have more than the max allowed, shuffle and trim them
                if len(tracepoints) > self.client_config.max_line_tps:
                    random.shuffle(tracepoints)
                    skipped = tracepoints[self.client_config.max_line_tps:]
                    tracepoints = tracepoints[:self.client_config.max_line_tps]

                # now order the tracepoint so we get them in the correct order for efficient processing
                ff_tps = [x for x in tracepoints if x.type == Breakpoint.STACK_TYPE]
                sf_tps = [x for x in tracepoints if x.type == Breakpoint.FRAME_TYPE or x.type == Breakpoint.LOG_POINT_TYPE]
                to_tps = [x for x in tracepoints if x.type == Breakpoint.TRACE_ONLY]
                nf_tps = [x for x in tracepoints if x.type == Breakpoint.NO_FRAME_TYPE]
                p_tps = [x for x in tracepoints if x.type == Breakpoint.PROFILE]

                if len(ff_tps) > 0:
                    processor.process_back_frame_vars = True

                if len(ff_tps) > 0 or len(sf_tps) > 0:
                    processor.process_frame(frame, line_start=line_start)
                else:
                    processor.process_frame(frame, line_start=line_start, process_vars=False)

                for tracepoint in ff_tps + sf_tps + to_tps + nf_tps:
                    tracepoint_map = self.bp_as_map(tracepoint)
                    self.add_rate_limit_info(tracepoint, tracepoint_map, rate_limit_copy)
                    # if we have spent too much time on this line, do not process watchers anymore and just post the hit
                    if self.time_exceeded(line_start, self.client_config.max_process_time):
                        tp_processor = processor.clone(tracepoint)
                        event = tp_processor.event_as_dict(tracepoint_map, log_msg=None, flags=['line_time_exceeded'])
                        self.context_service.send_event(event)
                    else:
                        tp_processor = processor.clone(tracepoint)
                        self.process_watches(tracepoint, frame, tp_processor)
                        log_msg = self.process_logs(tracepoint, frame, tp_processor)
                        event = tp_processor.event_as_dict(tracepoint_map, log_msg)
                        if 'line_hook' in tracepoint.args:
                            if current_thread.ident in self.callbacks:
                                self.callbacks[current_thread.ident].append({
                                    "event": event,
                                    "processor": tp_processor,
                                    "tp": tracepoint
                                })
                            else:
                                self.callbacks[current_thread.ident] = deque([{
                                    "event": event,
                                    "processor": tp_processor,
                                    "tp": tracepoint
                                }])
                        else:
                            self.context_service.send_event(event)

                if len(p_tps) > 0:
                    service = ProfilerService(self.context_service, frame, current_thread, config)
                    for tracepoint in p_tps:
                        tp_processor = processor.clone(tracepoint)
                        self.process_watches(tracepoint, frame, tp_processor)
                        log_msg = self.process_logs(tracepoint, frame, tp_processor)
                        service.add_tracepoint(tracepoint, tp_processor, log_msg)
                    profiling_thread = threading.Thread(target=service.start)
                    profiling_thread.setDaemon(True)
                    profiling_thread.setName("NerdVision - Profiler")
                    profiling_thread.start()

                # Post a stub to indicate the line was hit but the tracepoints where trimmed
                if skipped is not None:
                    self.context_service.send_skipped(skipped)

        return self.trace_call

    def add_rate_limit_info(self, bp, bp_map, rate_limit_copy):
        rate_limit_info = rate_limit_copy[bp.breakpoint_id]
        bp_map['args']['suppressed_count'] = rate_limit_info['suppressed_count']
        # reset suppressed count here rather than below since now we added it to the bp dict
        rate_limit_info['suppressed_count'] = 0
        # I dont think this is an issue as another breakpoint is unlikely to have the same bp id and if
        # the rate limit tracker is cleared when none are being processed it will remove the old copies
        self.rate_limit_tracker = rate_limit_copy

    def next_id(self):
        self.var_id = self.var_id + 1
        return self.var_id

    def process_request(self, response):
        self.process_request_common([Breakpoint.from_grpc(data) for data in response.breakpoints])

    def process_request_serverless(self, breakpoints):
        self.process_request_common([Breakpoint.from_json(data) for data in breakpoints])

    def process_request_common(self, breakpoints):
        our_logger.debug("Processing breakpoints %s", breakpoints)
        new_breakpoints = {}
        for _breakpoint in breakpoints:
            basename = os.path.basename(_breakpoint.rel_path)
            if basename in new_breakpoints:
                new_breakpoints[basename].append(_breakpoint)
            else:
                new_breakpoints[basename] = [_breakpoint]
        self.breakpoints = new_breakpoints
        # Decision made for now just clean the rate limits for everything when new breakpoints come in
        self.rate_limit_tracker = {}
        our_logger.debug("New breakpoint configuration %s", self.breakpoints)

    def breakpoints_for(self, filename):
        basename = os.path.basename(filename)

        if settings.is_point_cut_debug_enabled():
            our_logger.debug("Searching for breakpoint for %s", basename)

        if basename in self.breakpoints:
            breakpoints_basename_ = self.breakpoints[basename]
            return breakpoints_basename_
        else:
            return []

    def find_match(self, breakpoints_for, lineno, frame, rate_limit_copy):
        switcher = {
            'count': 0,
            'stack': False,
            'no_frame': False,
            'frame': False,
            'tps': []
        }

        for bp in breakpoints_for:
            if bp.line_no == lineno and self.condition_matches(bp, frame) and self.can_fire(bp, rate_limit_copy):
                switcher['count'] += 1
                if bp.type in switcher:
                    switcher[bp.type] = True
                else:
                    switcher['frame'] = True
                switcher['tps'].append(bp)

        return switcher

    def can_fire(self, bp, rate_limit_copy):
        if self.rate_limit_hit(bp, rate_limit_copy):
            return False

        if bp.fire_count >= 0:
            if rate_limit_copy[bp.breakpoint_id]['fire_count'] >= bp.fire_count:
                return False
            rate_limit_copy[bp.breakpoint_id]['fire_count'] += 1
        return True

    def rate_limit_hit(self, bp, rate_limit_copy):
        millis = int(round(time.time() * 1000))
        rate_limit = bp.args.get('rate_limit', settings.nv_settings['bp_rate_limit'])

        if bp.breakpoint_id in rate_limit_copy:
            bp_data = rate_limit_copy[bp.breakpoint_id]

            if (millis - bp_data['last_fired']) < int(rate_limit):
                bp_data['suppressed_count'] += 1
                return True
            else:
                bp_data['last_fired'] = millis
                return False

        rate_limit_copy[bp.breakpoint_id] = {'last_fired': millis,
                                             'suppressed_count': 0,
                                             'fire_count': 0}
        return False

    @staticmethod
    def condition_matches(bp, frame):
        if bp.condition is None or bp.condition == "":
            # There is no condition so return True
            return True
        our_logger.debug("Executing condition evaluation: %s", bp.condition)
        try:
            result = eval(bp.condition, None, frame.f_locals)
            our_logger.debug("Condition result: %s", result)
            if result:
                return True
            return False
        except Exception:
            our_logger.exception("Error evaluating condition %s", bp.condition)
            return False

    @staticmethod
    def process_log_watch(processor, log_watch):
        for watch in log_watch:
            BreakpointService.process_watch(log_watch[watch], processor, watch)

    @staticmethod
    def process_watch(eval_result, processor, watch, watch_name=None):
        watcher = Watcher(watch if watch_name is None else watch_name, watch)
        processor.process_watch_variable_breadth_first(watcher, eval_result)
        processor.add_watcher(watcher)

    @staticmethod
    def process_watches(bp, frame, processor):
        watches = bp.named_watchers
        for watch in watches:
            watch_ = watches[watch]
            our_logger.debug("Evaluating watcher: %s -> %s", watch, watch_)
            if watch_ != "":
                try:
                    eval_result = eval(watch_, None, frame.f_locals)
                    BreakpointService.process_watch(eval_result, processor, watch_, watch)
                except Exception as e:
                    our_logger.exception("Error evaluating watcher %s", watch_)
                    BreakpointService.process_watch(e, processor, watch_, watch)

    def process_log_point(self, bp_log, frame):
        logger = logging.getLogger(bp_log.args.get('logger_name', 'nerdvision'))

        try:
            log_msg = self.format_log(bp_log.args['log_msg'], frame.f_locals)
            logger \
                .log(level=self.as_log_int(bp_log.args.get('log_level', "INFO")),
                     msg=log_msg['log_msg'])
            return log_msg
        except Exception as e:
            message = None
            if logger is not None and BreakpointService.str2bool(bp_log.args.get('log_on_error', "False")):
                message = self.escape_message(bp_log.args['log_msg'])
                logger.error("[nerd.vision] Processing log message '%s' failed with error '%s'.", message, e)
                if BreakpointService.str2bool(bp_log.args.get('log_frame_on_error', "False")):
                    logger.error("[nerd.vision] Variables at frame: %s", frame.f_locals)
            return {'log_msg': message, 'watch_result': None}

    @staticmethod
    def str2bool(v):
        return str(v).lower() in ("yes", "true", "t", "1")

    @staticmethod
    def as_log_int(log_level):
        return logging.getLevelName(log_level)

    @staticmethod
    def format_log(msg, f_locals):
        watch_result = {}

        class FormatDict(dict):
            def __missing__(self, key):
                return "{%s}" % key

        import string

        class FormatExtractor(string.Formatter):
            def get_field(self, field_name, args, kwargs):
                try:
                    eval_result = eval(field_name, None, f_locals)
                    watch_result[field_name] = eval_result
                    return eval_result, field_name
                except Exception:
                    our_logger.exception("Error evaluating log msg %s", field_name)
                    eval_result, field_name_res = super(FormatExtractor, self).get_field(field_name, args, kwargs)
                    watch_result[field_name] = eval_result
                    return eval_result, field_name

        if f_locals:
            log_msg = "[nerd.vision] %s" % FormatExtractor().vformat(msg, (), FormatDict(f_locals))
        else:
            log_msg = "[nerd.vision] %s" % msg

        return {
            'watch_result': watch_result,
            'log_msg': log_msg
        }

    @staticmethod
    def escape_message(param):
        return param.replace("{", "{{").replace("}", "}}")

    @staticmethod
    def bp_as_map(bp):
        return Breakpoint.as_json(bp)

    def process_logs(self, tracepoint, frame, tp_processor):
        if 'log_msg' not in tracepoint.args:
            return None
        if tracepoint.args['log_msg'] == '':
            return None
        point = self.process_log_point(tracepoint, frame)
        log_msg_ = point['log_msg']
        log_watch_result = point['watch_result']
        if log_watch_result is None:
            return log_msg_

        BreakpointService.process_log_watch(tp_processor, log_watch_result)
        return log_msg_

    @staticmethod
    def time_exceeded(line_start, max_process_time, now=None):
        if now is None:
            now = Utils.time_ms()
        duration = now - line_start
        return duration > max_process_time

    def process_callbacks(self, frame, event, arg, current_thread):
        line_start = Utils.time_ms()
        data = self.callbacks[current_thread.ident].pop()

        # check that the frame is at the same point as the start
        if not self.frame_matches(frame, data):
            self.callbacks[current_thread.ident].append(data)
            return

        tracepoint = data['tp']
        if tracepoint.args['line_hook'] == Breakpoint.LINE_HOOK_DATA_RIGHT:
            config = BreakpointConfig([tracepoint])
            processor = FrameProcessor(config, client_config=self.client_config)

            # If type is stack then process back frames
            processor.process_back_frame_vars = (tracepoint.type == Breakpoint.STACK_TYPE)

            # if type is frame or stack process vars
            proc_vars = (tracepoint.type == Breakpoint.FRAME_TYPE or tracepoint.type == Breakpoint.STACK_TYPE)
            processor.process_frame(frame, line_start=line_start, process_vars=proc_vars)

            tp_processor = processor.clone(tracepoint)
            self.process_watches(tracepoint, frame, tp_processor)
            log_msg = self.process_logs(tracepoint, frame, tp_processor)
            tracepoint_map = self.bp_as_map(tracepoint)
            right_event = tp_processor.event_as_dict(tracepoint_map, log_msg)
            data['event'] = right_event

        data['event']['end_ts'] = Utils.time_ms()

        if event == "exception" and arg is not None:
            error = ErrorHandler.create_nv_error(arg[0], arg[1], arg[2])
            data['event']['exception'] = error.as_dict()
            data['event']['tags']['error'] = error.type

        self.context_service.send_event(data['event'])

        if len(self.callbacks[current_thread.ident]) == 0:
            del self.callbacks[current_thread.ident]

    @staticmethod
    def frame_matches(frame, data):
        filename = frame.f_code.co_filename
        func_name = frame.f_code.co_name

        stacktrace_frame = data['event']['stacktrace'][0]
        return stacktrace_frame['filename'] == filename and stacktrace_frame['methodname'] == func_name
