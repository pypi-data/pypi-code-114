from __future__ import annotations
from typing import Callable, Sequence, Any
import json

import numpy as np
import tensorflow as tf

from sknlp.vocab import Vocab
from .nlp_dataset import NLPDataset
from .bert_mixin import BertDatasetMixin


def _combine_xy(x, y):
    return ((x, y),)


def _combine_xyz(x, y, z):
    return ((x, y, z),)


def _combine_xy_z(x, y, z):
    return ((x, y), z)


class TaggingDataset(NLPDataset):
    def __init__(
        self,
        vocab: Vocab,
        labels: Sequence[str],
        segmenter: str | None = None,
        X: Sequence[Any] | None = None,
        y: Sequence[Any] | None = None,
        csv_file: str | None = None,
        in_memory: bool = True,
        has_label: bool = True,
        output_format: str = "global_pointer",
        max_length: int | None = None,
        text_dtype: tf.DType = tf.int64,
        label_dtype: tf.DType = tf.int32,
        **kwargs,
    ):
        self.output_format = output_format
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
            na_value="",
            text_dtype=text_dtype,
            label_dtype=label_dtype,
            **kwargs,
        )

    @property
    def y(self) -> list[list[str]]:
        if not self.has_label:
            return []
        return [
            json.loads(data[-1].decode("UTF-8"))
            for data in self._original_dataset.as_numpy_iterator()
        ]

    def y_row_to_col(self, y: Sequence[Any]) -> list[Sequence[str]]:
        if isinstance(y[0], (list, tuple)):
            y = [json.dumps(yi) for yi in y]
        return [y]

    @property
    def batch_padding_shapes(self) -> list[tuple]:
        shapes = [(None,), (None,), (None,)]
        if self.output_format == "global_pointer":
            shapes[-1] = (None, None, None)
        return shapes[: None if self.has_label else -1]

    def py_label_transform(self, label: tf.Tensor, tokens: list[str]) -> np.ndarray:
        label = super().py_label_transform(label)
        length = tokens.index(self.vocab.eos) + 1  # type_id == 0

        tokens = tokens[1 : length - 1]
        start_mapping, end_mapping = self.vocab.create_ichar2itoken_mapping(tokens)
        chunks = json.loads(label)
        if self.output_format == "bio":
            labels = np.zeros(length, dtype=np.int32)
            for chunk_start, chunk_end, chunk_label in chunks:
                chunk_start = start_mapping[chunk_start] + 1
                chunk_end = end_mapping[chunk_end] + 1
                if chunk_start == 0 or chunk_end == 0:
                    continue

                labels[chunk_start] = self.label2idx[chunk_label] * 2 - 1
                for i in range(chunk_start + 1, chunk_end + 1):
                    labels[i] = self.label2idx[chunk_label] * 2
        else:
            labels = np.zeros((len(self.label2idx), length, length), dtype=np.int32)
            for chunk_start, chunk_end, chunk_label in chunks:
                chunk_start = start_mapping[chunk_start] + 1
                chunk_end = end_mapping[chunk_end] + 1
                if chunk_start == 0 or chunk_end == 0:
                    continue

                labels[self.label2idx[chunk_label], chunk_start, chunk_end] = 1
        return labels

    def py_transform(self, *data: list[np.ndarray]) -> list[np.ndarray]:
        tokens, type_ids = self.py_text_transform(
            data[: -1 if self.has_label else None]
        )
        token_ids = np.array(self.vocab.token2idx(tokens), dtype=np.int64)
        transformed_data = [token_ids, np.array(type_ids, dtype=np.int64)]
        if self.has_label:
            transformed_data.append(self.py_label_transform(data[-1], tokens))
        return transformed_data

    def batchify(
        self,
        batch_size: int,
        shuffle: bool = True,
        training: bool = True,
        shuffle_buffer_size: int | None = None,
        after_batch: Callable | None = None,
    ) -> tf.data.Dataset:
        if after_batch is None:
            if not self.has_label:
                after_batch = _combine_xy
            elif self.output_format == "bio":
                if training:
                    after_batch = _combine_xyz
                else:
                    after_batch = _combine_xy_z
            else:
                after_batch = _combine_xy_z
        return super().batchify(
            batch_size,
            shuffle=shuffle,
            training=training,
            shuffle_buffer_size=shuffle_buffer_size,
            after_batch=after_batch,
        )


class BertTaggingDataset(BertDatasetMixin, TaggingDataset):
    def py_transform(self, *data: list[np.ndarray | bytes]) -> list[np.ndarray]:
        tokens, type_ids = self.py_text_transform(data[0])
        token_ids = np.array(self.vocab.token2idx(tokens), dtype=np.int64)
        transformed_data = [token_ids, np.array(type_ids, dtype=np.int64)]
        if self.has_label:
            transformed_data.append(self.py_label_transform(data[-1], tokens))
        return transformed_data