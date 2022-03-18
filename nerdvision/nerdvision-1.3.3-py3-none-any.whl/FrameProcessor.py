import logging
import os
import time

from nerdvision.models.Breakpoint import Breakpoint
from nerdvision.models.EventSnapshot import EventSnapshot, SnapshotFrame, Variable, VariableId
from nerdvision.models.Node import Node

our_logger = logging.getLogger("nerdvision")

NO_CHILD_TYPES = [
    'str',
    'int',
    'float',
    'bool',
    'type',
    'module',
    'unicode',
    'long'
]

LIST_LIKE_TYPES = [
    'frozenset',
    'set',
    'list',
    'tuple',
]

ITER_LIKE_TYPES = [
    'list_iterator',
    'listiterator',
    'list_reverseiterator',
    'listreverseiterator',
]


class FrameProcessor(object):
    def __init__(self, config, client_config):
        self.client_config = client_config
        self.config = config
        self.max_depth = config.max_var_depth
        self.max_list_len = config.max_collection_size
        self.max_str_length = config.max_string_length
        self.max_vars = config.max_variables
        self.event = EventSnapshot()
        self.watchers = []
        self.v_id = 0
        self.var_lookup = {}
        self.var_cache = {}
        self.process_back_frame_vars = False
        self.has_time_exceeded = False
        self.tags = dict(client_config.tags)

    def flags(self, additional=None):
        if additional is None:
            additional = []
        flags = additional
        if self.has_time_exceeded:
            flags.append('time_exceeded')
        if self.v_id >= self.max_vars:
            flags.append('vars_exceeded')
        return flags

    def add_watcher(self, watcher):
        self.watchers.append(watcher)

    def next_id(self):
        self.v_id = self.v_id + 1
        return self.v_id

    def process_frame(self, frame, line_start, process_vars=True):
        lineno = frame.f_lineno
        filename = frame.f_code.co_filename
        basename = os.path.basename(filename)
        func_name = frame.f_code.co_name

        f_locals = frame.f_locals
        _self = f_locals.get('self', None)
        class_name = basename
        if _self is not None:
            class_name = _self.__class__.__name__

        snapshot_frame = SnapshotFrame(class_name, func_name, lineno, filename, 0)

        self.event.add_frame(snapshot_frame)

        # only process  vars if we are under the time limit
        if process_vars and not self.time_exceeded(line_start):
            self.process_frame_variables_breadth_first(f_locals, snapshot_frame)

        back_ = frame.f_back
        if back_ is not None:
            self.process_frame(back_, line_start, self.process_back_frame_vars)

    def search_consumer(self, node):
        value = node.get_value()
        if value is None:
            return True
        node_key_ = value['name']

        if self.v_id >= self.max_vars:
            our_logger.debug('Skipping var no: %d; key: %s;', self.v_id, node_key_)
            return False

        node_value_ = value['value']
        variable, process_children = self.process_variable_breadth_first(node_key_, node_value_)
        node.get_parent().add_child(variable)

        if not self.var_lookup[variable.id].flagged('redacted') and process_children:
            children = self.process_children_breadth_first(variable.id, node_value_, node.depth, variable)
            node.add_children(children)
        return True

    def process_watch_variable_breadth_first(self, watch, variable):
        def add_watch_var(var):
            watch.add_variable(var)

        parent = Node()
        parent.add_child = add_watch_var

        root = Node(value=None, children=[Node(value={'name': watch.expression, 'value': variable}, parent=parent)],
                    parent=parent)

        Node.breadth_first_search(root, self.search_consumer)

    def process_frame_variables_breadth_first(self, f_locals, snapshot_frame):
        def add_frame_var(var):
            snapshot_frame.add_variable(var)

        parent = Node()
        parent.add_child = add_frame_var

        child_nodes = self.process_dict_breadth_first(parent, f_locals)

        root = Node(value=None, children=child_nodes, parent=parent)

        Node.breadth_first_search(root, self.search_consumer)

    def truncate_string(self, string):
        return string[:self.max_str_length], len(string) > self.max_str_length

    def clone(self, tracepoint):
        # type: (Breakpoint) -> FrameProcessor
        processor = FrameProcessor(self.config, self.client_config)
        processor.var_cache = dict(self.var_cache)
        processor.var_lookup = dict(self.var_lookup)
        processor.event = self.event
        processor.v_id = self.v_id

        if tracepoint.type == Breakpoint.FRAME_TYPE or tracepoint.type == Breakpoint.LOG_POINT_TYPE:
            processor.trim_frame_vars()
        if tracepoint.type == Breakpoint.TRACE_ONLY:
            processor.trim_frame_vars(-1)
        if tracepoint.type == Breakpoint.NO_FRAME_TYPE or tracepoint.type == Breakpoint.PROFILE:
            processor.trim_frame_vars(-1)
            processor.trim_frames()
            processor.var_lookup = {}

        # add the basic tags for the snapshot
        processor.tags['line'] = tracepoint.line_no
        processor.tags['file'] = tracepoint.rel_path
        processor.tags['type'] = tracepoint.type
        if 'workspace' in tracepoint.args:
            processor.tags['workspace'] = tracepoint.args['workspace']

        if 'tag_keys' in tracepoint.args:
            tag_keys = tracepoint.args['tag_keys'].split(',')
            for tag_key_raw in tag_keys:
                tag_key = tag_key_raw.strip()
                if tag_key in tracepoint.args:
                    processor.tags[tag_key] = tracepoint.args[tag_key]

        return processor

    def time_exceeded(self, line_start):
        duration = int(round(time.time() * 1000)) - line_start
        self.has_time_exceeded = duration > self.config.max_tp_process_time
        return self.has_time_exceeded

    def trim_frame_vars(self, start_from=0):
        for i, sf in enumerate(self.event.stack_trace):
            if i > start_from:
                sf.variables = []

    def trim_frames(self):
        self.event.stack_trace = []

    def event_as_dict(self, tracepoint, log_msg=None, flags=None):
        as_dict = self.event.as_dict()
        as_dict['breakpoint'] = tracepoint
        as_dict['log_msg'] = log_msg
        as_dict['var_lookup'] = self.format_var_lookup(self.var_lookup)
        as_dict['flags'] = self.flags(flags)
        as_dict['named_watches'] = [watch.as_dict() for watch in self.watchers]
        as_dict['tags'] = self.tags

        return as_dict

    @staticmethod
    def format_var_lookup(var_lookup):
        for k, v in var_lookup.items():
            var_lookup[k] = v.as_dict()
        return var_lookup

    def process_variable_breadth_first(self, node_key_, node_value_):
        hash_ = str(id(node_value_))

        if hash_ in self.var_cache:
            var_id = self.var_cache[hash_]
            return VariableId(var_id, node_key_), False

        var_id = self.next_id()
        collection = False
        type_ = type(node_value_)
        if self.client_config.black_list(node_key_):
            our_logger.debug("Variable named: %s is blacklisted.", node_key_)
            truncate_string, truncated = '[REDACTED]', False
            variable = Variable(var_id, str(node_key_), type_, truncate_string, hash_)
            variable.flag('redacted')
        else:
            if type_ is int or type_ is float or type_ is bool or type_.__name__ == 'long' or node_value_ is None:
                truncate_string, truncated = node_value_, False
            elif type_.__name__ in ITER_LIKE_TYPES:
                truncate_string, truncated = 'Object of type: %s' % type_, False
            elif type_ is dict or type_.__name__ in LIST_LIKE_TYPES:
                truncate_string, truncated = 'Size: %s' % len(node_value_), False
                collection = True
            else:
                truncate_string, truncated = self.truncate_string(str(node_value_))
            variable = Variable(var_id, str(node_key_), type_, truncate_string, hash_)
            if truncated:
                variable.flag('truncated')

        if collection:
            variable.flag('collection')

        self.var_cache[hash_] = var_id
        self.var_lookup[var_id] = variable
        return VariableId(var_id, node_key_), True

    def process_children_breadth_first(self, parent_id, value, curr_depth, var):
        type_ = type(value)
        if value is None or type_.__name__ in NO_CHILD_TYPES:
            return []

        def parent_add_child(child):
            self.var_lookup[parent_id].add_variable(child)

        parent_node = Node()
        parent_node.add_child = parent_add_child

        if curr_depth + 1 >= self.max_depth:
            var_from_lookup = self.var_lookup[var.id]
            var_from_lookup.flag('depth')
            return []
        return self.find_children_for_parent(parent_node, value)

    def find_children_for_parent(self, parent_node, value):
        type_ = type(value)
        if type_ is dict:
            return self.process_dict_breadth_first(parent_node, value)
        elif type_.__name__ in LIST_LIKE_TYPES:
            return self.process_list_breadth_first(parent_node, value)
        elif type_.__name__ in ITER_LIKE_TYPES:
            return self.process_iterable_breadth_first(parent_node, value)
        elif isinstance(value, Exception):
            return self.process_list_breadth_first(parent_node, value.args)
        elif hasattr(value, '__dict__'):
            return self.process_dict_breadth_first(parent_node, value.__dict__)
        else:
            our_logger.debug("Unknown type processed %s", type_)
            return []

    def process_dict_breadth_first(self, parent_node, value):
        # we wrap the keys() in a call to list to prevent concurrent changes
        return [Node(value={'name': key, 'value': value[key]}, parent=parent_node) for key in list(value.keys()) if
                not self.client_config.skip_list(key) and key in value]

    def process_list_breadth_first(self, parent_node, value):
        nodes = []
        total = 0
        for val_ in tuple(value):
            if total >= self.max_list_len:
                parent_node.flag('list_truncated')
                break
            nodes.append(Node(value={'name': total, 'value': val_}, parent=parent_node))
            total += 1
        return nodes

    # todo this needs to be checked, does it affect the position of the iterable
    def process_iterable_breadth_first(self, parent_node, value):
        nodes = []
        end = VariableId(-1, 'end')
        val = next(value, end)
        total = 0
        while val is not end:
            if total > self.max_list_len:
                parent_node.flag('list_truncated')
                break
            nodes.append(Node(value={'name': total, 'value': val}, parent=parent_node))
            val = next(value, end)
            total += 1
        return nodes
