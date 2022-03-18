from __future__ import annotations
from typing import Sequence, Callable

import tensorflow as tf
import numpy as np


class BertDatasetMixin:
    def tf_transform_before_py_transform(
        self, *data: Sequence[tf.Tensor]
    ) -> list[tf.Tensor]:
        tokens = self.tokenize(data[: -1 if self.has_label else None])
        if self.has_label:
            return [tokens, data[-1]]
        return [tokens]

    def py_text_transform(
        self, tokens_tensor: np.ndarray
    ) -> tuple[list[str], list[int]]:
        tokens_list: list[list[str]] = [
            [
                token.decode("UTF-8")
                for token in tokens
                if token.decode("UTF-8") != self.vocab.pad
            ]
            for tokens in tokens_tensor.tolist()
        ]
        trimmed_tokens_list = self._round_robin_trim(
            tokens_list, self.max_length - (len(tokens_list) + 1)
        )
        tokens: list[str] = [self.vocab.bos]
        type_ids: list[int] = [0]
        for i, trimmed_tokens in enumerate(trimmed_tokens_list):
            type_id = i
            if i >= 1:
                type_id = 1
            tokens.extend(trimmed_tokens)
            type_ids.extend([type_id for _ in range(len(trimmed_tokens))])
            tokens.append(self.vocab.eos)
            type_ids.append(type_id)
        return tokens, type_ids

    def py_transform(self, *data: list[np.ndarray | bytes]) -> list[np.ndarray]:
        tokens, type_ids = self.py_text_transform(data[0])
        token_ids = np.array(self.vocab.token2idx(tokens), dtype=np.int64)
        transformed_data = [token_ids, np.array(type_ids, dtype=np.int64)]
        if self.has_label:
            transformed_data.append(self.py_label_transform(data[-1]))
        return transformed_data