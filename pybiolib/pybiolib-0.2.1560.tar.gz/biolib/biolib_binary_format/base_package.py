from abc import ABC, abstractmethod

from biolib.typing_utils import Optional


class BasePackage(ABC):
    _VERSION = 1


class IndexableBuffer(ABC):

    def __init__(self):
        self.pointer = 0

    @abstractmethod
    def get_data(self, start: int, end: int) -> bytes:
        pass

    def get_data_as_string(self, start: int, end: int) -> str:
        return self.get_data(start=start, end=end).decode()

    def get_data_as_int(self, start: int, end: int) -> int:
        return int.from_bytes(bytes=self.get_data(start=start, end=end), byteorder='big')

    def get_data_with_pointer(self, length_bytes: int) -> bytes:
        data = self.get_data(self.pointer, self.pointer+length_bytes)
        self.pointer += length_bytes
        return data

    def get_data_with_pointer_as_int(self, length_bytes: int) -> int:
        data = self.get_data_with_pointer(length_bytes)
        return int.from_bytes(data, 'big')

# Will be used once we interact with files in S3
# class S3IndexableBuffer(IndexableBuffer):
#
#     def __init__(self, data: bytes):
#         super().__init__()
#         self._length_bytes = len(data)
#
#         requests.put(url='s3', data=data, timeout=11111111)
#
#     def get_data(self, start: int, end: int) -> bytes:
#         pass
#
#     def append_data(self, data: bytes) -> None:
#         pass


class InMemoryIndexableBuffer(IndexableBuffer):

    def __init__(self, data: bytes):
        super().__init__()
        self._buffer = data
        self._length_bytes = len(data)

    def get_data(self, start: int, end: int) -> bytes:
        return self._buffer[start:end]

    def __len__(self):
        return self._length_bytes


class File:

    def __init__(self, path: str, buffer: IndexableBuffer, start: int, end: int):
        self._path = path
        self._buffer = buffer
        self._start = start
        self._end = end

        self._data: Optional[bytes] = None

    @property
    def path(self) -> str:
        return self._path

    def get_data(self) -> bytes:
        if self._data is None:
            self._data = self._buffer.get_data(start=self._start, end=self._end)

        return self._data
