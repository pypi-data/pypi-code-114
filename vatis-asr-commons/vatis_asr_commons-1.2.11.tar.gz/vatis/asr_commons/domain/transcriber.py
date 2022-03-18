import numpy as np

from typing import List, Tuple, Optional, Type


class DataPacket:
    def __init__(self, headers=None):
        self.headers = {} if headers is None else headers.copy()

    def get_header(self, name, default=None, dtype: Type = str):
        if name not in self.headers:
            return default

        if default is not None:
            dtype = type(default)

        if dtype == bool:
            return str(self.headers.get(name)) == 'True'
        else:
            return dtype(self.headers.get(name))

    def set_header(self, name, value):
        self.headers[name] = value


class StringPacket(DataPacket):
    def __init__(self, data: str, headers=None):
        super().__init__(headers)
        self.data = data


class ByteDataPacket(DataPacket):
    def __init__(self, data: bytes, headers=None):
        super().__init__(headers)
        self.data = data


class TranscriptionPacket(DataPacket):
    def __init__(self, transcript: str, headers=None):
        super().__init__(headers)
        self.transcript = transcript


class Word:
    def __init__(self, word: str, start_time_millis: float, end_time_millis: float, speaker: Optional[int] = None,
                 confidence: float = 0):
        self.word: str = word
        self.start_time: float = start_time_millis
        self.end_time: float = end_time_millis
        self.speaker: int = speaker
        self.confidence: float = confidence


class TimestampedTranscriptionPacket(TranscriptionPacket):
    """
    Packet that contains the transcript with the timestamps associated to each word.

    Params:
     - words: list of transcribed words
     - headers: headers of the packet
    """
    def __init__(self, words: List[Word], headers=None, transcript=None):
        transcript = transcript if transcript is not None else ' '.join([word.word for word in words])
        super().__init__(transcript, headers)

        self.words = words


class NdArrayDataPacket(DataPacket):
    def __init__(self, data: np.ndarray, headers=None):
        super().__init__(headers)
        self.data: np.ndarray = data


class LogitsDataPacket(NdArrayDataPacket):
    def __init__(self, data: np.ndarray, timestep_duration: float, headers=None):
        super().__init__(data, headers)
        self.timestep_duration = timestep_duration


class SpacedLogitsDataPacket(LogitsDataPacket):
    def __init__(self, data: np.ndarray, timestep_duration: float, spaces: List[Tuple[int, int]], headers=None):
        super().__init__(data, timestep_duration, headers)
        self.spaces = spaces

