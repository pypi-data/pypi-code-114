from __future__ import annotations
from typing import Sequence, Callable

import numpy as np
import tensorflow as tf

from sknlp.vocab import Vocab
from .nlp_dataset import NLPDataset
from .bert_mixin import BertDatasetMixin
from .utils import serialize_example


def _combine_xy(token_ids, type_ids, label):
    return ((token_ids, type_ids), label)


def _combine_x(token_ids, type_ids):
    return ((token_ids, type_ids),)


class ClassificationDataset(NLPDataset):
    def __init__(
        self,
        vocab: Vocab,
        labels: Sequence[str],
        segmenter: str | None = None,
        X: Sequence[str] | Sequence[Sequence[str]] | None = None,
        y: Sequence[str] | None = None,
        csv_file: str | None = None,
        in_memory: bool = True,
        has_label: bool = True,
        is_multilabel: bool = False,
        max_length: int | None = None,
        text_dtype: tf.DType = tf.int64,
        label_dtype: tf.DType = tf.int32,
        **kwargs,
    ):
        self.labels = list(labels)
        self.is_multilabel = is_multilabel
        self.label2idx = dict(zip(labels, range(len(labels))))
        super().__init__(
            vocab,
            segmenter=segmenter,
            X=X,
            y=y,
            csv_file=csv_file,
            in_memory=in_memory,
            has_label=has_label,
            max_length=max_length,
            na_value="NULL",
            text_dtype=text_dtype,
            label_dtype=label_dtype,
            **kwargs,
        )

    @property
    def y(self) -> list[str] | list[list[str]]:
        if not self.has_label:
            return []
        return [
            data[-1].decode("UTF-8").split("|")
            if self.is_multilabel
            else data[-1].decode("UTF-8")
            for data in self._original_dataset.as_numpy_iterator()
        ]

    def y_row_to_col(self, y: Sequence[Sequence[str] | str]) -> list[Sequence[str]]:
        if isinstance(y[0], (list, tuple)):
            y = "|".join(y)
        return [y]

    @property
    def batch_padding_shapes(self) -> list[tuple[int | None]]:
        shapes = [(None,), (None,), (None,)]
        return shapes[: None if self.has_label else -1]

    @property
    def batch_padding_values(self) -> list[int]:
        values = [np.int64(self.vocab[self.vocab.pad]), np.int64(0), -1]
        return values[: None if self.has_label else -1]

    def py_label_transform(self, label: bytes) -> np.ndarray:
        _label = super().py_label_transform(label)
        if self.is_multilabel:
            labels = _label.split("|")
        else:
            labels = [_label]
        label_ids = [
            self.label2idx[label] for label in labels if label in self.label2idx
        ]
        if len(label_ids) == 0:
            # 没有标签的异常数据， 填入0， 以保证正常训练
            # 抛出异常可能更合适
            label_ids = [0]
        return np.array(label_ids, dtype=np.int32)

    def batchify(
        self,
        batch_size: int,
        shuffle: bool = True,
        training: bool = True,
        shuffle_buffer_size: int | None = None,
        after_batch: Callable | None = None,
    ) -> tf.data.Dataset:
        if after_batch is None:
            after_batch = _combine_xy if self.has_label else _combine_x
        return super().batchify(
            batch_size,
            shuffle=shuffle,
            training=training,
            shuffle_buffer_size=shuffle_buffer_size,
            after_batch=after_batch,
        )

    def to_tfrecord(self, filename: str) -> None:
        def func(text: np.ndarray, label: np.ndarray):
            return tf.reshape(
                serialize_example(
                    (self._text_transform(text), self._label_transform(label)),
                    ("tensor", "tensor"),
                ),
                (),
            )

        tf_writer = tf.data.experimental.TFRecordWriter(filename)
        tf_writer.write(
            self._dataset.map(
                lambda t, l: tf.py_function(func, inp=[t, l], Tout=tf.string),
                num_parallel_calls=tf.data.experimental.AUTOTUNE,
            )
        )

    @classmethod
    def from_tfrecord(cls, filename: str) -> tf.data.Dataset:
        def func(record: tf.Tensor):
            parsed_record = tf.io.parse_single_example(
                record,
                {
                    "feature0": tf.io.FixedLenFeature([], tf.string, default_value=""),
                    "feature1": tf.io.FixedLenFeature([], tf.string, default_value=""),
                },
            )
            return (
                tf.io.parse_tensor(parsed_record["feature0"], tf.int32),
                tf.io.parse_tensor(parsed_record["feature1"], tf.float32),
            )

        return tf.data.TFRecordDataset(filename).map(func)


class BertClassificationDataset(BertDatasetMixin, ClassificationDataset):
    pass