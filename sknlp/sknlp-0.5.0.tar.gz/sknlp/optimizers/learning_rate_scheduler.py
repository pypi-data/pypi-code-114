from __future__ import annotations
from typing import Any

import math

import tensorflow as tf


@tf.keras.utils.register_keras_serializable(package="sknlp")
class CosineDecayWithWarmup(tf.keras.optimizers.schedules.CosineDecay):
    def __init__(
        self,
        initial_learning_rate: float,
        warmup_steps: int,
        decay_steps: int,
        alpha: float = 0.0,
        name: str | None = None,
    ) -> None:
        super().__init__(initial_learning_rate, decay_steps, alpha=alpha, name=name)
        self.warmup_steps = warmup_steps

    def __call__(self, step: tf.Tensor) -> tf.Tensor:
        with tf.name_scope(self.name or "CosineDecay"):
            initial_learning_rate = tf.convert_to_tensor(
                self.initial_learning_rate, name="initial_learning_rate"
            )
            dtype = initial_learning_rate.dtype
            warmup_steps = tf.cast(self.warmup_steps, dtype)
            decay_steps = tf.cast(self.decay_steps, dtype)
            global_step_recomp = tf.cast(step, dtype)
            global_step_recomp = tf.minimum(global_step_recomp, decay_steps)
            return tf.multiply(
                initial_learning_rate,
                tf.cond(
                    tf.less_equal(global_step_recomp + 1, warmup_steps),
                    lambda: (global_step_recomp + 1) / warmup_steps,
                    lambda: self.alpha
                    + (1 - self.alpha)
                    * 0.5
                    * (1.0 + tf.cos(math.pi * global_step_recomp / decay_steps)),
                ),
            )

    def get_config(self) -> dict[str, Any]:
        return {**super().get_config(), "warmup_steps": self.warmup_steps}
