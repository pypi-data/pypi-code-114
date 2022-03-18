import os


class ProfileNode(object):
    def __init__(self, frame):
        self.line_no = frame['lineno']
        self.file_name = frame['filename']
        self.func_name = frame['func_name']
        self.count = 0
        self.duration = 0
        self.self_duration = 0
        self.children = []

    def add_node(self, frame, duration):
        self.count += 1
        next_ = frame['next']
        if next_ is None:
            self.self_duration += duration
            return
        else:
            self.duration += duration
        current_node = [child for child in self.children if
                        child.file_name == next_['filename'] and child.line_no == next_['lineno']]
        if len(current_node) > 0:
            current_node[0].add_node(next_, duration)
        else:
            node = ProfileNode(next_)
            self.children.append(node)
            node.add_node(next_, duration)

    def as_json(self):
        return {
            'classname': os.path.basename(self.file_name),
            'linenumber': self.line_no,
            'filename': self.file_name,
            'methodname': self.func_name,
            'count': self.count,
            'duration': self.duration,
            'self_duration': self.self_duration,
            'nodes': [node.as_json() for node in self.children]
        }
