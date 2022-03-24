"""
Classes which are serializable to tuples to allow use in tensorflow datasets
"""
from dataclasses import dataclass

import tensorflow as tf


@dataclass(frozen=True, order=True)
class TfRange:
    """
    An object for slicing tensors
    """
    start: int = 0
    end: int = 0

    def slice(self, sequence):
        if self.end == 0:
            return sequence[tf.cast(self.start, tf.int32):]
        else:
            return sequence[tf.cast(self.start, tf.int32):tf.cast(self.end, tf.int32)]

    @classmethod
    def build(cls, x):
        return cls(x[0], x[1])

    @classmethod
    def build_single_frame(cls, frame):
        frame = int(frame)
        return cls(frame, frame+1)

    def __iter__(self):
        yield from (self.start, self.end)

    def __str__(self):
        return f"SequenceRange{self.start, None if self.end == 0 else self.end}"
