# *_*coding:utf-8 *_*

from typing import Dict, Any
from tensorflow import keras

from .conditional_random_field import KConditionalRandomField
from .behdanau_attention import BahdanauAttention  # type: ignore

L = keras.layers
L.BahdanauAttention = BahdanauAttention
L.KConditionalRandomField = KConditionalRandomField


def resigter_custom_layers(custom_objects: Dict[str, Any]) -> Dict[str, Any]:
    custom_objects['KConditionalRandomField'] = KConditionalRandomField
    custom_objects['BahdanauAttention'] = BahdanauAttention
    return custom_objects
