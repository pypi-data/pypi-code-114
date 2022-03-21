from threading import Lock

import os

from uuid import uuid4

from imagination.decorator import service


@service.registered()
class Console:
    """
    Virtual Console

    This class is a workaround to allow external processes capture the output through it.
    """
    def __init__(self):
        self.__id = str(uuid4())
        self.__output_buffer = ''
        self.__output_lock = Lock()

    def flush_output(self) -> str:
        snapshot: str = ''
        with self.__output_lock:
            snapshot += self.__output_buffer
            self.__output_buffer = ''
        return snapshot

    def print(self, content, end='\n'):
        with self.__output_lock:
            print(content, end=end)
            self.__output_buffer += f'{content}{end}'