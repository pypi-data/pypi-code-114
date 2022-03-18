from __future__ import annotations
from typing import Any, Sequence

import tensorflow as tf
import tensorflow_text as tftext


@tf.keras.utils.register_keras_serializable(package="sknlp")
class PreprocessingLayer(tf.keras.layers.Layer):
    def __init__(
        self,
        bos_id: int,
        eos_id: int,
        max_length: int = 120,
        name: str = "preprocess",
        **kwargs,
    ) -> None:
        self.bos_id = bos_id
        self.eos_id = eos_id
        self.max_length = max_length
        super().__init__(name=name, **kwargs)

    def build(self, input_shape: tf.TensorShape) -> None:
        self.trimmer = tftext.RoundRobinTrimmer(self.max_length)
        super().build(input_shape)

    def call(self, inputs: tf.Tensor) -> None:
        inputs = tf.unstack(inputs, axis=1)
        token_ids_list = tf.nest.map_structure(
            lambda x: tf.ragged.boolean_mask(x, x != 0), inputs
        )
        token_ids, type_ids = tftext.combine_segments(
            self.trimmer.trim(token_ids_list),
            start_of_sequence_id=self.bos_id,
            end_of_segment_id=self.eos_id,
        )
        return token_ids.to_tensor(), type_ids.to_tensor()

    def get_config(self) -> dict[str, Any]:
        return {
            **super().get_config(),
            "bos_id": self.bos_id,
            "eos_id": self.eos_id,
            "max_length": self.max_length,
        }


@tf.keras.utils.register_keras_serializable(package="sknlp")
class BertPreprocessingLayer(tf.keras.layers.Layer):
    def __init__(
        self,
        vocab: Sequence[str],
        cls_token: str = "[CLS]",
        sep_token: str = "[SEP]",
        max_length: int = 510,
        name: str = "bert_tokenize",
        **kwargs,
    ) -> None:
        vocab: list = list(vocab)
        self.cls_token = cls_token
        self.sep_token = sep_token
        self.max_length = max_length
        if cls_token not in vocab:
            vocab.append(cls_token)
        if sep_token not in vocab:
            vocab.append(sep_token)

        self.max_chars_per_token = 1
        for i, token in enumerate(vocab):
            if token == cls_token:
                self.cls_id = i
            if token == sep_token:
                self.sep_id = i
            self.max_chars_per_token = max(self.max_chars_per_token, len(token))
        self.vocab = vocab
        super().__init__(name=name, **kwargs)

    def build(self, input_shape: tf.TensorShape) -> None:
        self.tokenizer = tftext.BertTokenizer(
            tf.lookup.StaticVocabularyTable(
                tf.lookup.KeyValueTensorInitializer(
                    self.vocab,
                    list(range(len(self.vocab))),
                    key_dtype=tf.string,
                    value_dtype=tf.int64,
                ),
                1,
            ),
            max_chars_per_token=self.max_chars_per_token,
        )
        self.trimmer = tftext.RoundRobinTrimmer(self.max_length)
        super().build(input_shape)

    def call(self, inputs: tf.Tensor) -> list[tf.Tensor]:
        # (batch_size, num_inputs) -> num_inputs * (batch_size, )
        inputs = tf.unstack(inputs, axis=1)
        ragged_tensors: list[
            tuple[tf.RaggedTensor, tf.RaggedTensor, tf.RaggedTensor]
        ] = tf.nest.flatten(
            tf.nest.map_structure(
                lambda x: self.tokenizer.tokenize_with_offsets(x), inputs
            )
        )
        token_ids_list = tf.nest.map_structure(
            lambda x: x.merge_dims(-2, -1), ragged_tensors[::3]
        )

        token_ids, type_ids = tftext.combine_segments(
            self.trimmer.trim(token_ids_list),
            start_of_sequence_id=self.cls_id,
            end_of_segment_id=self.sep_id,
        )
        tensors: list[tf.Tensor] = [
            token_ids.to_tensor(),
            tf.where(type_ids.to_tensor() == 0, x=0, y=1),
        ]
        starts = ragged_tensors[1]
        ends = ragged_tensors[2]
        tensors.append(starts.merge_dims(-2, -1).to_tensor())
        tensors.append(ends.merge_dims(-2, -1).to_tensor())
        return tensors

    def get_config(self) -> dict[str, Any]:
        return {
            **super().get_config(),
            "vocab": self.vocab,
            "cls_token": self.cls_token,
            "sep_token": self.sep_token,
            "max_length": self.max_length,
        }
