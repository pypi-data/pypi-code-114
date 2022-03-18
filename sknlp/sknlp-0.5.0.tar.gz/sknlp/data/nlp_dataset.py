from __future__ import annotations
from typing import Callable, Any, Sequence

import pandas as pd
import tensorflow as tf
import numpy as np

from sknlp.vocab import Vocab
from .tokenizer import get_tokenizer


class NLPDataset:
    def __init__(
        self,
        vocab: Vocab,
        segmenter: str | None = None,
        X: Sequence[str] | Sequence[Sequence[str]] | None = None,
        y: Sequence[str] | None = None,
        csv_file: str | None = None,
        in_memory: bool = True,
        has_label: bool = True,
        text_normalization: dict[str, str] = {"letter_case": "lowercase"},
        max_length: int | None = None,
        na_value: str = "",
        text_dtype: tf.DType = tf.string,
        label_dtype: tf.DType = tf.string,
        **kwargs
    ) -> None:
        if X is None and csv_file is None:
            raise ValueError("Either `X` or `csv_file` may not be None.")
        self.in_memory = in_memory
        self.na_value = na_value
        self.text_normalization = text_normalization
        self.tokenize = get_tokenizer(segmenter, vocab).tokenize
        self.vocab = vocab
        self.max_length = max_length or 99999
        self.text_dtype = text_dtype
        self.label_dtype = label_dtype

        self.has_label = has_label
        self.na_value = na_value
        ncols = 2
        if csv_file is not None:
            self._original_dataset, self._size, ncols = self.load_csv(
                csv_file,
                "\t",
                in_memory,
                self.na_value,
            )
        else:
            self.has_label = has_label and y is not None
            df = self.Xy_to_dataframe(X, y=y)
            self._size = df.shape[0]
            ncols = df.shape[1]
            self._original_dataset = self.dataframe_to_dataset(df, self.na_value)
        self.num_texts = ncols - self.has_label
        self._original_dataset = self._original_dataset.map(
            self.normalize, num_parallel_calls=tf.data.AUTOTUNE
        )

    @property
    def size(self) -> int:
        if self._size is not None:
            return self._size

        i = 0
        for _ in self._original_dataset:
            i += 1
        self._size = i
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        if self._size is None:
            self._size = value

    @property
    def X(self) -> list[Any]:
        x = []
        for data in self._original_dataset.as_numpy_iterator():
            texts = data[: -1 if self.has_label else None]
            if len(texts) == 1:
                x.append(texts[0].decode("UTF-8"))
            else:
                x.append([text.decode("UTF-8") for text in texts])
        return x

    @property
    def y(self) -> list[str]:
        if not self.has_label:
            return []
        return [
            data[-1].decode("UTF-8")
            for data in self._original_dataset.as_numpy_iterator()
        ]

    def X_row_to_col(self, X: Sequence[Any]) -> list[Sequence[str]]:
        if isinstance(X[0], str):
            return [X]
        return list(zip(*X))

    def y_row_to_col(self, y: Sequence[Any]) -> list[Sequence[Any]]:
        return [y]

    def Xy_to_dataframe(
        self,
        X: Sequence[str] | Sequence[Sequence[str]],
        y: Sequence[Any] | None = None,
    ) -> pd.DataFrame:
        X = self.X_row_to_col(X)
        if y is not None:
            y = self.y_row_to_col(y)
        return pd.DataFrame(zip(*X, *y) if y is not None else zip(*X))

    @property
    def batch_padding_shapes(self) -> Sequence[tuple[int | None]] | None:
        return None

    @property
    def batch_padding_values(self) -> list[int | float] | None:
        return None

    def normalize_letter_case(self, data: tf.Tensor) -> tf.Tensor:
        letter_case = self.text_normalization.get("letter_case", "keep")
        if letter_case == "lowercase":
            return tf.strings.lower(data, encoding="utf-8")
        elif letter_case == "uppercase":
            return tf.strings.upper(data, encoding="utf-8")
        return data

    def normalize_text(self, *data: list[tf.Tensor]) -> list[tf.Tensor]:
        return [self.normalize_letter_case(d) for d in data]

    def normalize_label(self, data: tf.Tensor) -> tf.Tensor:
        return data

    def normalize(self, *data: list[tf.Tensor]) -> list[tf.Tensor]:
        normalized = self.normalize_text(*data[: -1 if self.has_label else None])
        if self.has_label:
            normalized.append(self.normalize_label(data[-1]))
        return normalized

    def _round_robin_trim(
        self, tokens_list: list[list[str]], max_length: int
    ) -> list[list[str]]:
        lengths = [len(tokens) for tokens in tokens_list]
        if sum(lengths) <= max_length:
            return tokens_list

        min_length = min(lengths)
        fill_length = min(min_length, max_length // len(lengths))
        trimmed_lengths = [fill_length] * len(lengths)

        remainder_length = max_length - fill_length * len(lengths)
        i = 0
        while remainder_length:
            if trimmed_lengths[i] < lengths[i]:
                trimmed_lengths[i] += 1
                remainder_length -= 1
            i = (i + 1) % len(lengths)
        return [tokens[:length] for tokens, length in zip(tokens_list, trimmed_lengths)]

    def py_text_transform(
        self, texts: Sequence[np.ndarray | bytes]
    ) -> tuple[list[str], list[int]]:
        tokens_list: list[list[str]] = [
            self.tokenize(text.decode("UTF-8")) for text in texts
        ]
        trimmed_tokens_list = self._round_robin_trim(
            tokens_list, self.max_length - (len(tokens_list) + 1)
        )
        tokens: list[str] = [self.vocab.bos]
        type_ids: list[int] = [0]
        for i, trimmed_tokens in enumerate(trimmed_tokens_list):
            tokens.extend(trimmed_tokens)
            type_ids.extend([i for _ in range(len(trimmed_tokens))])
            tokens.append(self.vocab.eos)
            type_ids.append(i)
        return tokens, type_ids

    def py_label_transform(self, label: np.ndarray | bytes) -> str | np.ndarray:
        return label.decode("UTF-8")

    def py_transform(self, *data: Sequence[np.ndarray | str]) -> list[np.ndarray | str]:
        tokens, type_ids = self.py_text_transform(
            data[: -1 if self.has_label else None]
        )
        token_ids = np.array(self.vocab.token2idx(tokens), dtype=np.int64)
        transformed_data = [token_ids, np.array(type_ids, dtype=np.int64)]
        if self.has_label:
            transformed_data.append(self.py_label_transform(data[-1]))
        return transformed_data

    def py_transform_out_dtype(self) -> list[tf.DType] | tf.DType:
        dtypes = [self.text_dtype, self.text_dtype, self.label_dtype]
        return dtypes[: None if self.has_label else -1]

    def tf_transform_before_py_transform(
        self, *data: Sequence[tf.Tensor]
    ) -> list[tf.Tensor]:
        return data

    def tf_transform_after_py_transform(
        self, *data: Sequence[tf.Tensor]
    ) -> list[tf.Tensor]:
        return data

    def shuffled_dataset(
        self, dataset: tf.data.Dataset, shuffle_buffer_size: int | None = None
    ) -> tf.data.Dataset:
        shuffle_buffer_size = shuffle_buffer_size or self.size or 100000
        return dataset.shuffle(shuffle_buffer_size)

    def batchify(
        self,
        batch_size: int,
        shuffle: bool = True,
        training: bool = True,
        shuffle_buffer_size: int | None = None,
        after_batch: Callable | None = None,
    ) -> tf.data.Dataset:
        dataset = self._original_dataset
        dataset = dataset.map(
            self.tf_transform_before_py_transform, num_parallel_calls=tf.data.AUTOTUNE
        )
        dataset = dataset.map(
            lambda *data: tf.numpy_function(
                self.py_transform,
                inp=data,
                Tout=self.py_transform_out_dtype(),
            )
        )
        dataset = dataset.map(
            self.tf_transform_after_py_transform, num_parallel_calls=tf.data.AUTOTUNE
        ).cache()
        if shuffle:
            dataset = self.shuffled_dataset(
                dataset, shuffle_buffer_size=shuffle_buffer_size
            )
        if self.batch_padding_shapes is None:
            dataset = dataset.batch(batch_size)
        else:
            padding_values = None
            if self.batch_padding_values is not None:
                padding_values = tuple(self.batch_padding_values)
            dataset = dataset.padded_batch(
                batch_size,
                padded_shapes=tuple(self.batch_padding_shapes),
                padding_values=padding_values,
            )
        if after_batch is not None:
            dataset = dataset.map(after_batch, num_parallel_calls=tf.data.AUTOTUNE)
        return dataset.prefetch(buffer_size=tf.data.AUTOTUNE)

    @classmethod
    def dataframe_to_dataset(cls, df: pd.DataFrame, na_value: str) -> tf.data.Dataset:
        df.fillna(na_value, inplace=True)
        return tf.data.Dataset.from_tensor_slices(tuple(df[col] for col in df.columns))

    @classmethod
    def load_csv(
        cls, filename: str, sep: str, in_memory: bool, na_value: str
    ) -> tuple[tf.data.Dataset, int | None, int]:
        if in_memory:
            df = pd.read_csv(filename, sep=sep, dtype="str", quoting=3, escapechar="\\")
            return (
                cls.dataframe_to_dataset(df, na_value=na_value),
                df.shape[0],
                df.shape[1],
            )

        df: pd.DataFrame = pd.read_csv(
            filename, sep=sep, dtype="str", quoting=3, escapechar="\\", nrows=1
        )
        return (
            tf.data.experimental.CsvDataset(
                filename,
                [tf.dtypes.string] * df.shape[1],
                header=True,
                field_delim=sep,
                na_value=na_value,
            ),
            None,
            df.shape[1],
        )
