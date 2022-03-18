import time

from nerdvision import agent_name, TYPES

if TYPES:
    from typing import Dict, Optional, Union, List


class NVErrorFrame(object):
    def __init__(self, class_name, func_name, line_no, source_file, source_line):
        # type: (str, str, int, str, str) -> None
        self.class_name = class_name  # type: str
        self.func_name = func_name  # type: str
        self.line_no = line_no  # type: int
        self.source_file = source_file  # type: str
        self.source_line = source_line  # type: str

    def as_dict(self):
        # type: () -> Dict[str,str]
        return {
            'classname': self.class_name,
            'methodname': self.func_name,
            'linenumber': self.line_no,
            'filename': self.source_file,
            'source': self.source_line
        }


class NVError(object):
    def __init__(self, _type, message):
        # type: (str, str) -> None
        self.id = None  # type: Optional[str]
        self.trace = []  # type: List[NVErrorFrame]
        self.type = _type  # type: str
        self.message = message  # type: str
        self.timestamp = int(time.time())  # type: int

    def add_frame(self, frame):
        # type: (NVErrorFrame) -> None
        self.trace.append(frame)

    def push_frame(self, frame):
        # type: (NVErrorFrame) -> None
        self.trace.insert(0, frame)

    def as_dict(self):
        # type: () -> Dict[str,Union[str,Dict[str,str]]]
        return {
            'id': self.id,
            'trace': [_frame.as_dict() for _frame in self.trace],
            'type': self.type,
            'message': self.message,
            'timestamp': self.timestamp,
            'source': agent_name
        }
