from __future__ import annotations
from typing import Optional, Any

import tensorflow as tf
from tensorflow.keras.metrics import Precision, Recall
from tensorflow_addons.metrics import FBetaScore

from sknlp.utils.tensor import pad2shape
from .utils import logits2pred


@tf.keras.utils.register_keras_serializable(package="sknlp")
class PrecisionWithLogits(Precision):
    def __init__(
        self,
        top_k: Optional[int] = None,
        class_id: Optional[int] = None,
        threshold: float = 0.5,
        name: str = "precision",
        dtype: Optional[tf.DType] = None,
        activation: str = "linear",
    ) -> None:
        super().__init__(
            thresholds=threshold,
            top_k=top_k,
            class_id=class_id,
            name=name,
            dtype=dtype,
        )
        self.activation = activation

    def update_state(
        self,
        y_true: tf.Tensor,
        y_logits: tf.Tensor,
        sample_weight: Optional[tf.Tensor] = None,
    ) -> None:
        y_pred = logits2pred(y_logits, self.activation)
        # y_pred = pad2shape(y_pred, tf.shape(y_true), value=0)
        super().update_state(y_true, y_pred, sample_weight=sample_weight)

    def get_config(self) -> dict[str, Any]:
        configs = super().get_config()
        configs.pop("thresholds", None)
        return {
            **configs,
            "threshold": self.thresholds,
            "activation": self.activation,
        }


@tf.keras.utils.register_keras_serializable(package="sknlp")
class SparsePrecisionWithLogits(PrecisionWithLogits):
    def update_state(
        self,
        y_true: tf.Tensor,
        y_logits: tf.Tensor,
        sample_weight: Optional[tf.Tensor] = None,
    ) -> None:
        y_pred = logits2pred(y_logits, self.activation)
        y_pred = y_pred > self.thresholds

        # 标签的padding使用-1, 通过+1和pred第一列填充0避免padding的影响
        y_true = tf.cast(y_true, tf.int32) + 1
        y_pred = tf.cast(y_pred, self.dtype)
        y_pred = tf.concat(
            [tf.zeros_like(y_pred[..., :1], dtype=self.dtype), y_pred], 1
        )

        def _weighted_sum(val, sample_weight):
            if sample_weight is not None:
                val = tf.math.multiply(val, tf.expand_dims(sample_weight, 1))
            return tf.expand_dims(tf.reduce_sum(val), 0)

        if self.class_id is not None:
            y_true = tf.where(y_true == self.class_id + 1, x=self.class_id + 1, y=0)
        tp = _weighted_sum(
            tf.gather(y_pred, y_true, batch_dims=1, axis=1), sample_weight
        )
        self.true_positives.assign_add(tp)
        if self.class_id is not None:
            y_pred = y_pred[..., self.class_id + 1, None]
        self.false_positives.assign_add(_weighted_sum(y_pred, sample_weight) - tp)


@tf.keras.utils.register_keras_serializable(package="sknlp")
class RecallWithLogits(Recall):
    def __init__(
        self,
        top_k: Optional[int] = None,
        class_id: Optional[int] = None,
        threshold: float = 0.5,
        name: str = "recall",
        dtype: Optional[tf.DType] = None,
        activation: str = "linear",
    ) -> None:
        super().__init__(
            thresholds=threshold,
            top_k=top_k,
            class_id=class_id,
            name=name,
            dtype=dtype,
        )
        self.activation = activation

    def update_state(
        self,
        y_true: tf.Tensor,
        y_logits: tf.Tensor,
        sample_weight: Optional[tf.Tensor] = None,
    ) -> None:
        y_pred = logits2pred(y_logits, self.activation)
        # y_pred = pad2shape(y_pred, tf.shape(y_true), value=0)
        super().update_state(y_true, y_pred, sample_weight=sample_weight)

    def get_config(self) -> dict[str, Any]:
        configs = super().get_config()
        configs.pop("thresholds", None)
        return {
            **configs,
            "threshold": self.thresholds,
            "activation": self.activation,
        }


@tf.keras.utils.register_keras_serializable(package="sknlp")
class SparseRecallWithLogits(RecallWithLogits):
    def update_state(
        self,
        y_true: tf.Tensor,
        y_logits: tf.Tensor,
        sample_weight: Optional[tf.Tensor] = None,
    ) -> None:
        y_pred = logits2pred(y_logits, self.activation)
        y_pred = y_pred > self.thresholds

        # 标签的padding使用-1, 通过+1和pred第一列填充0避免padding的影响
        y_true = tf.cast(y_true, tf.int32) + 1
        y_pred = tf.cast(y_pred, self.dtype)
        y_pred = tf.concat(
            [tf.zeros_like(y_pred[..., :1], dtype=self.dtype), y_pred], 1
        )

        def _weighted_sum(val, sample_weight):
            if sample_weight is not None:
                val = tf.math.multiply(val, tf.expand_dims(sample_weight, 1))
            return tf.expand_dims(tf.reduce_sum(val), 0)

        if self.class_id is not None:
            y_true = tf.where(y_true == self.class_id + 1, x=self.class_id + 1, y=0)
        tp = _weighted_sum(
            tf.gather(y_pred, y_true, batch_dims=1, axis=1), sample_weight
        )
        fn = _weighted_sum(
            tf.cast(
                tf.logical_and(
                    tf.gather(y_pred, y_true, batch_dims=1, axis=1) == 0,
                    y_true != 0,
                ),
                self.dtype,
            ),
            sample_weight,
        )
        self.true_positives.assign_add(tp)
        self.false_negatives.assign_add(fn)


@tf.keras.utils.register_keras_serializable(package="sknlp")
class FBetaScoreWithLogits(FBetaScore):
    def __init__(
        self,
        num_classes: int,
        average: str = "micro",
        beta: float = 1.0,
        class_id: Optional[int] = None,
        threshold: float = 0.5,
        name: str = "fbeta_score",
        dtype: Optional[tf.DType] = None,
        activation: str = "linear",
    ) -> None:
        super().__init__(
            num_classes,
            average=average,
            beta=beta,
            threshold=threshold,
            name=name,
            dtype=dtype,
        )
        self.class_id = class_id
        self.activation = activation

    def update_state(
        self,
        y_true: tf.Tensor,
        y_logits: tf.Tensor,
        sample_weight: Optional[tf.Tensor] = None,
    ) -> None:
        y_pred = logits2pred(y_logits, self.activation)
        # y_pred = pad2shape(y_pred, tf.shape(y_true), value=0)
        if self.class_id is not None:
            y_true = y_true[..., self.class_id]
            y_pred = y_pred[..., self.class_id]
        super().update_state(y_true, y_pred, sample_weight=sample_weight)

    def get_config(self) -> dict[str, Any]:
        return {
            **super().get_config(),
            "activation": self.activation,
            "class_id": self.class_id,
        }


@tf.keras.utils.register_keras_serializable(package="sknlp")
class SparseFBetaScoreWithLogits(FBetaScoreWithLogits):
    def update_state(
        self,
        y_true: tf.Tensor,
        y_logits: tf.Tensor,
        sample_weight: Optional[tf.Tensor] = None,
    ) -> None:
        y_pred = logits2pred(y_logits, self.activation)
        y_pred = y_pred > self.threshold

        # 标签的padding使用-1, 通过+1和pred第一列填充0避免padding的影响
        y_true = tf.cast(y_true, tf.int32) + 1
        y_pred = tf.cast(y_pred, self.dtype)
        y_pred = tf.concat(
            [tf.zeros_like(y_pred[..., :1], dtype=self.dtype), y_pred], 1
        )

        def _weighted_sum(val, sample_weight):
            if sample_weight is not None:
                val = tf.math.multiply(val, tf.expand_dims(sample_weight, 1))
            return tf.reduce_sum(val, axis=self.axis)

        if self.class_id is not None:
            y_true = tf.where(y_true == self.class_id + 1, x=self.class_id + 1, y=0)
        tp = _weighted_sum(
            tf.gather(y_pred, y_true, batch_dims=1, axis=1), sample_weight
        )
        fn = _weighted_sum(
            tf.cast(
                tf.logical_and(
                    tf.gather(y_pred, y_true, batch_dims=1, axis=1) == 0,
                    y_true != 0,
                ),
                self.dtype,
            ),
            sample_weight,
        )
        self.true_positives.assign_add(tp)
        self.false_negatives.assign_add(fn)
        if self.class_id is not None:
            y_pred = y_pred[..., self.class_id + 1, None]
        self.false_positives.assign_add(_weighted_sum(y_pred, sample_weight) - tp)
        self.weights_intermediate.assign_add(
            _weighted_sum(tf.cast(y_true, tf.float32), sample_weight)
        )