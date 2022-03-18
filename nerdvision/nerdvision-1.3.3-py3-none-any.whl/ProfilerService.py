import os
import sys
import time

from nerdvision.models.ProfileNode import ProfileNode


class ProfilerService(object):
    def __init__(self, context_service, initial_frame, thread, config):
        self.thread = thread
        self.context_service = context_service
        self.tracepoints = []
        self.run_time = config.max_profile_time
        self.interval = config.profile_interval / 1000
        self.profile_node = ProfileNode(ProfilerService.trace(initial_frame))

    def add_tracepoint(self, tracepoint, processor, log_msg):
        self.tracepoints.append({
            'tracepoint': tracepoint,
            'log_msg': log_msg,
            'watchers': processor.watchers,
            'var_lookup': processor.var_lookup,
            'flags': processor.flags(),
            'config': {
                'interval': str(self.interval)
            }
        })

    def start(self):
        start_time = int(round(time.time() * 1000))
        last_run = start_time
        while self.check_time(start_time):
            # noinspection PyProtectedMember,PyUnresolvedReferences
            thread_frame = sys._current_frames()
            frame = thread_frame.get(self.thread.ident)
            trace = ProfilerService.trace(frame)
            self.profile_node.add_node(trace, int(round(time.time() * 1000)) - last_run)
            last_run = int(round(time.time() * 1000))
            time.sleep(self.interval)

        profile_data = self.as_json(start_time)
        for tracepoint in self.tracepoints:
            profile_data.update(tracepoint)
            self.context_service.send_profile(profile_data)

    @staticmethod
    def trace(frame):
        frames = []
        current_frame = frame
        previous_frame = None
        while current_frame is not None:
            lineno = current_frame.f_lineno
            filename = current_frame.f_code.co_filename
            basename = os.path.basename(filename)
            func_name = current_frame.f_code.co_name
            frames_ = {
                'lineno': lineno,
                'filename': filename,
                'basename': basename,
                'func_name': func_name,
                'next': previous_frame
            }
            frames.append(frames_)
            previous_frame = frames_
            current_frame = current_frame.f_back
        frames.reverse()
        return frames[0]

    def check_time(self, start_time):
        now = int(round(time.time() * 1000))
        duration = now - start_time
        return duration <= self.run_time

    def as_json(self, start_time):
        return {
            'thread': {
                'name': self.thread.name,
                'id': self.thread.ident,
                'daemon': self.thread.isDaemon(),
            },
            'start_time': start_time,
            'profile': self.profile_node.as_json()
        }
