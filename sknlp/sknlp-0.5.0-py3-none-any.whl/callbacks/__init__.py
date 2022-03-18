from __future__ import annotations
from typing import Any

import tensorflow as tf

from .tagging_fscore_metric import TaggingFScoreMetric


def default_supervised_model_callbacks(
    has_validation_dataset: bool = False,
    enable_early_stopping: bool = False,
    early_stopping_monitor: str = "val_loss",
    early_stopping_monitor_direction: str = "min",
    early_stopping_patience: int = 3,
    early_stopping_min_delta: float = 0.0,
    early_stopping_use_best_epoch: bool = True,
    checkpoint: str | None = None,
    log_file: str = None,
    verbose: int = 2,
) -> list[tf.keras.callbacks.Callback]:
    callbacks = []
    if enable_early_stopping and has_validation_dataset:
        callbacks.append(
            tf.keras.callbacks.EarlyStopping(
                monitor=early_stopping_monitor,
                min_delta=early_stopping_min_delta,
                patience=early_stopping_patience,
                mode=early_stopping_monitor_direction,
                restore_best_weights=early_stopping_use_best_epoch,
                verbose=verbose,
            )
        )
    if checkpoint is not None:
        options = tf.saved_model.SaveOptions(experimental_custom_gradients=False)
        callbacks.append(
            tf.keras.callbacks.ModelCheckpoint(
                checkpoint,
                monitor=early_stopping_monitor,
                mode=early_stopping_monitor_direction,
                save_best_only=has_validation_dataset,
                options=options,
                verbose=verbose,
            )
        )
    if log_file is not None:
        callbacks.append(tf.keras.callbacks.CSVLogger(log_file))
    return callbacks


__all__ = [
    "TaggingFScoreMetric",
    "default_supervised_model_callbacks",
]