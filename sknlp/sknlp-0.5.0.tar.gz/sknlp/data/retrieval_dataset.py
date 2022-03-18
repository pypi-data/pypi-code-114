from __future__ import annotations
from typing import Any, Sequence, Optional, Callable

import tensorflow as tf
import numpy as np

from sknlp.vocab import Vocab
from .nlp_dataset import NLPDataset
from .bert_mixin import BertDatasetMixin


def _generate_y(x):
    return tf.reshape(x, (-1, tf.shape(x)[-1])), tf.range(tf.shape(x)[0])


class RetrievalDataset(NLPDataset):
    def __init__(
        self,
        vocab: Vocab,
        labels: Sequence[str],
        segmenter: Optional[str] = None,
        X: Optional[Sequence[Any]] = None,
        y: Optional[Sequence[Any]] = None,
        csv_file: Optional[str] = None,
        in_memory: bool = True,
        has_label: bool = True,
        max_length: Optional[int] = None,
        text_dtype: tf.DType = tf.int64,
        label_dtype: tf.DType = tf.int64,
        **kwargs,
    ):
        self.label2idx = dict(zip(labels, range(len(labels))))
        super().__init__(
            vocab,
            segmenter,
            X=X,
            y=y,
            csv_file=csv_file,
            in_memory=in_memory,
            has_label=has_label,
            max_length=max_length,
            na_value="",
            text_dtype=text_dtype,
            label_dtype=label_dtype,
        )

    @property
    def X(self) -> list[Any]:
        return [
            data[0].decode("UTF-8")
            for data in self._original_dataset.as_numpy_iterator()
        ]

    @property
    def y(self) -> list[str]:
        if not self.has_label:
            return []
        return [
            [d.decode("UTF-8") for d in data[1:]]
            for data in self._original_dataset.as_numpy_iterator()
        ]

    def y_row_to_col(self, y: Sequence[str | Sequence[str]]) -> list[Sequence[str]]:
        return self.X_row_to_col(y)

    @property
    def batch_padding_shapes(self) -> list[tuple]:
        return (None, None)

    def normalize(self, *data: list[tf.Tensor]) -> list[tf.Tensor]:
        return self.normalize_text(*data)

    def py_label_transform(self, label: bytes) -> int:
        return self.label2idx[super().py_label_transform(label)]

    def py_transform(self, *data: Sequence[np.ndarray]) -> np.ndarray:
        token_ids_list = [
            self.vocab.token2idx(self.py_text_transform([d])[0]) for d in data
        ]
        return tf.keras.preprocessing.sequence.pad_sequences(
            token_ids_list, padding="post", dtype="int64"
        )

    def py_transform_out_dtype(self) -> tf.DType:
        return self.text_dtype

    def tf_transform_after_py_transform(self, data: tf.Tensor) -> tf.Tensor:
        if self.has_label:
            return data
        else:
            return tf.concat([data, data], 0)

    def batchify(
        self,
        batch_size: int,
        shuffle: bool = True,
        training: bool = True,
        shuffle_buffer_size: Optional[int] = None,
        after_batch: Optional[Callable] = None,
    ) -> tf.data.Dataset:
        if after_batch is None:
            after_batch = _generate_y
        return super().batchify(
            batch_size,
            shuffle=shuffle,
            shuffle_buffer_size=shuffle_buffer_size,
            after_batch=after_batch,
        )


def _reshape_x(*data):
    x = data[0]
    reshaped_x = tf.reshape(x, (-1, tf.shape(x)[-1]))
    if len(data) == 1:
        return [reshaped_x]
    else:
        return [reshaped_x, data[-1]]


class RetrievalEvaluationDataset(RetrievalDataset):
    def __init__(
        self,
        vocab: Vocab,
        labels: Sequence[str],
        segmenter: Optional[str] = None,
        X: Optional[Sequence[Any]] = None,
        y: Optional[Sequence[Any]] = None,
        csv_file: Optional[str] = None,
        in_memory: bool = True,
        has_label: bool = True,
        max_length: Optional[int] = None,
        text_dtype: tf.DType = tf.int64,
        label_dtype: tf.DType = tf.int64,
        **kwargs,
    ):
        super().__init__(
            vocab,
            labels,
            segmenter=segmenter,
            X=X,
            y=y,
            csv_file=csv_file,
            in_memory=in_memory,
            has_label=has_label,
            max_length=max_length,
            text_dtype=text_dtype,
            label_dtype=label_dtype,
            **kwargs,
        )

    @property
    def y(self) -> list[str]:
        if not self.has_label:
            return []
        return [data[-1] for data in self._original_dataset.as_numpy_iterator()]

    def y_row_to_col(self, y: Sequence[str]) -> list[Sequence[str]]:
        return super(RetrievalDataset, self).y_row_to_col(y)

    @property
    def batch_padding_shapes(self) -> list[tuple]:
        return [(None, None), ()][: None if self.has_label else -1]

    def normalize(self, *data: list[tf.Tensor]) -> list[tf.Tensor]:
        return super(RetrievalDataset, self).normalize(*data)

    def py_transform(self, *data: Sequence[tf.Tensor]) -> list[Any]:
        token_ids_list = [
            self.vocab.token2idx(self.py_text_transform([d])[0])
            for d in data[: -1 if self.has_label else None]
        ]
        transformed_data = [
            tf.keras.preprocessing.sequence.pad_sequences(
                token_ids_list, padding="post", dtype="int64"
            )
        ]
        if self.has_label:
            transformed_data.append(self.py_label_transform(data[-1]))
        return transformed_data

    def tf_transform_after_py_transform(
        self, *data: Sequence[tf.Tensor]
    ) -> Sequence[tf.Tensor]:
        return data

    def py_transform_out_dtype(self) -> list[tf.DType]:
        return [self.text_dtype, self.label_dtype][: None if self.has_label else -1]

    def batchify(
        self,
        batch_size: int,
        shuffle: bool = True,
        training: bool = True,
        shuffle_buffer_size: Optional[int] = None,
        after_batch: Optional[Callable] = None,
    ) -> tf.data.Dataset:
        if after_batch is None:
            after_batch = _reshape_x
        return super().batchify(
            batch_size,
            shuffle=shuffle,
            training=training,
            shuffle_buffer_size=shuffle_buffer_size,
            after_batch=after_batch,
        )


def _bert_generate_y(x):
    reshaped_x = tf.reshape(x, (-1, tf.shape(x)[-1]))
    return (
        (reshaped_x, tf.zeros_like(reshaped_x, dtype=tf.int64)),
        tf.range(tf.shape(x)[0]),
    )


class BertRetrievalDataset(BertDatasetMixin, RetrievalDataset):
    @property
    def batch_padding_shapes(self) -> tuple:
        return super(BertDatasetMixin, self).batch_padding_shapes

    def tf_transform_before_py_transform(self, *data: Sequence[tf.Tensor]) -> tf.Tensor:
        return self.tokenize(data)

    def py_transform_out_dtype(self) -> tf.DType:
        return self.text_dtype

    def py_text_transform(self, tokens_tensor: np.ndarray) -> np.ndarray:
        cls_id: int = self.vocab["[CLS]"]
        sep_id: int = self.vocab["[SEP]"]
        pad_id: int = self.vocab[self.vocab.pad]
        token_ids_list = []
        for _, tokens in enumerate(tokens_tensor.tolist()):
            token_ids = self.vocab.token2idx(
                [token.decode("UTF-8") for token in tokens][: self.max_length]
            )
            token_ids = [tid for tid in token_ids if tid != pad_id]
            token_ids.insert(0, cls_id)
            token_ids.append(sep_id)
            token_ids_list.append(token_ids)
        return tf.keras.preprocessing.sequence.pad_sequences(
            token_ids_list, padding="post", dtype="int64"
        )

    def py_transform(self, data: np.ndarray) -> np.ndarray:
        return self.py_text_transform(data)

    def batchify(
        self,
        batch_size: int,
        shuffle: bool = True,
        training: bool = True,
        shuffle_buffer_size: Optional[int] = None,
        after_batch: Optional[Callable] = None,
    ) -> tf.data.Dataset:
        if after_batch is None:
            after_batch = _bert_generate_y
        return super().batchify(
            batch_size,
            shuffle=shuffle,
            training=training,
            shuffle_buffer_size=shuffle_buffer_size,
            after_batch=after_batch,
        )


def _bert_reshape_x(*data):
    x = data[0]
    reshaped_x = tf.reshape(x, (-1, tf.shape(x)[-1]))
    type_ids = tf.zeros_like(reshaped_x, dtype=tf.int64)
    if len(data) == 1:
        return ((reshaped_x, type_ids),)
    else:
        return ((reshaped_x, type_ids), data[-1])


class BertRetrievalEvaluationDataset(BertDatasetMixin, RetrievalEvaluationDataset):
    @property
    def batch_padding_shapes(self) -> tuple:
        return super(BertDatasetMixin, self).batch_padding_shapes

    def py_transform_out_dtype(self) -> list[tf.DType]:
        return [self.text_dtype, self.label_dtype][: None if self.has_label else -1]

    def py_text_transform(self, tokens_tensor: np.ndarray) -> list[np.ndarray]:
        cls_id: int = self.vocab["[CLS]"]
        sep_id: int = self.vocab["[SEP]"]
        pad_id: int = self.vocab[self.vocab.pad]
        token_ids_list = []
        for _, tokens in enumerate(tokens_tensor.tolist()):
            token_ids = self.vocab.token2idx(
                [token.decode("UTF-8") for token in tokens][: self.max_length]
            )
            token_ids = [tid for tid in token_ids if tid != pad_id]
            token_ids.insert(0, cls_id)
            token_ids.append(sep_id)
            token_ids_list.append(token_ids)
        return tf.keras.preprocessing.sequence.pad_sequences(
            token_ids_list, padding="post", dtype="int64"
        )

    def py_transform(self, *data: list[np.ndarray | bytes]) -> list[np.ndarray]:
        transformed_data = [self.py_text_transform(data[0])]
        if self.has_label:
            transformed_data.append(self.py_label_transform(data[-1]))
        return transformed_data

    def batchify(
        self,
        batch_size: int,
        shuffle: bool = True,
        training: bool = True,
        shuffle_buffer_size: Optional[int] = None,
        after_batch: Optional[Callable] = None,
    ) -> tf.data.Dataset:
        if after_batch is None:
            after_batch = _bert_reshape_x
        return super().batchify(
            batch_size,
            shuffle=shuffle,
            training=training,
            shuffle_buffer_size=shuffle_buffer_size,
            after_batch=after_batch,
        )