# used to convert dict to breakpoint type for serverless
class Breakpoint(object):
    STACK_TYPE = 'stack'
    FRAME_TYPE = 'frame'
    LOG_POINT_TYPE = 'log_point'
    NO_FRAME_TYPE = 'no_frame'
    TRACE_ONLY = 'trace'
    PROFILE = 'profile'

    LINE_HOOK_DATA_RIGHT = 'data_right'
    LINE_HOOK_DATA_LEFT = 'data_left'

    def __init__(self, dictionary):
        self.breakpoint_id = None
        self.workspace_id = None
        self.line_no = None
        self.rel_path = None
        self.src_type = None
        self.condition = None
        self.fire_count = None
        self.type = None
        self.state = None,
        self.id = None,
        self.created = None,
        self.metadata = {}
        self.named_watchers = {}
        if 'named_watches' in dictionary:
            self.named_watchers = dictionary['named_watches']
        self.args = {}
        for k, v in dictionary.items():
            setattr(self, k, v)

    @staticmethod
    def as_json(bp):
        # type: (Breakpoint) -> dict
        return {
            'breakpoint_id': bp.breakpoint_id,
            'workspace_id': bp.workspace_id,
            'rel_path': bp.rel_path,
            'line_no': bp.line_no,
            'condition': bp.condition,
            'src_type': bp.src_type,
            'named_watches': dict(bp.named_watchers),
            'args': dict(bp.args),
            'fire_count': bp.fire_count,
            'type': bp.type
        }

    @staticmethod
    def from_grpc(bp):
        return Breakpoint(Breakpoint.as_json(bp))

    @staticmethod
    def from_json(bp):
        return Breakpoint(bp)

    def __str__(self):
        # type: () -> str
        return str(Breakpoint.as_json(self))


class BreakpointConfig(object):
    DEFAULT_MAX_VAR_DEPTH = 5
    DEFAULT_MAX_VARIABLES = 1000
    DEFAULT_MAX_COLLECTION_SIZE = 10
    DEFAULT_MAX_STRING_LENGTH = 1024
    DEFAULT_MAX_WATCH_VARS = 100
    DEFAULT_MAX_TP_PROCESS_TIME = 100
    DEFAULT_MAX_PROFILE_TIME = 1000
    DEFAULT_PROFILE_INTERVAL = 10

    def __init__(self, breakpoints):
        # set to initial -1
        self.max_var_depth = -1
        self.max_variables = -1
        self.max_collection_size = -1
        self.max_string_length = -1
        self.max_watch_vars = -1
        self.max_tp_process_time = -1
        self.max_profile_time = -1
        self.profile_interval = -1

        # process config list
        for bp in breakpoints:
            config = bp.args
            self.max_var_depth = BreakpointConfig.get_max_or_default(config, 'MAX_VAR_DEPTH', self.max_var_depth)
            self.max_variables = BreakpointConfig.get_max_or_default(config, 'MAX_VARIABLES', self.max_variables)
            self.max_collection_size = BreakpointConfig.get_max_or_default(config, 'MAX_COLLECTION_SIZE',
                                                                           self.max_collection_size)
            self.max_string_length = BreakpointConfig.get_max_or_default(config, 'MAX_STRING_LENGTH', self.max_string_length)
            self.max_watch_vars = BreakpointConfig.get_max_or_default(config, 'MAX_WATCH_VARS', self.max_watch_vars)
            self.max_tp_process_time = BreakpointConfig.get_max_or_default(config, 'MAX_TP_PROCESS_TIME',
                                                                           self.max_tp_process_time)
            self.max_profile_time = BreakpointConfig.get_max_or_default(config, 'MAX_PROFILE_TIME', self.max_profile_time)
            self.profile_interval = BreakpointConfig.get_max_or_default(config, 'PROFILE_INTERVAL', self.profile_interval)

        self.max_var_depth = BreakpointConfig.DEFAULT_MAX_VAR_DEPTH if self.max_var_depth == -1 else self.max_var_depth
        self.max_variables = BreakpointConfig.DEFAULT_MAX_VARIABLES if self.max_variables == -1 else self.max_variables
        self.max_collection_size = BreakpointConfig.DEFAULT_MAX_COLLECTION_SIZE if self.max_collection_size == -1 else self.max_collection_size
        self.max_string_length = BreakpointConfig.DEFAULT_MAX_STRING_LENGTH if self.max_string_length == -1 else self.max_string_length
        self.max_watch_vars = BreakpointConfig.DEFAULT_MAX_WATCH_VARS if self.max_watch_vars == -1 else self.max_watch_vars
        self.max_tp_process_time = BreakpointConfig.DEFAULT_MAX_TP_PROCESS_TIME if self.max_tp_process_time == -1 else self.max_tp_process_time
        self.max_profile_time = BreakpointConfig.DEFAULT_MAX_PROFILE_TIME if self.max_profile_time == -1 else self.max_profile_time
        self.profile_interval = BreakpointConfig.DEFAULT_PROFILE_INTERVAL if self.profile_interval == -1 else self.profile_interval

    @staticmethod
    def get_max_or_default(config, key, default_value):
        if key in config:
            return max(int(config[key]), default_value)
        return default_value
