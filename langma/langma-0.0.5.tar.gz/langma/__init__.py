# *_*coding:utf-8 *_*

from .__version__ import version, __version__
from typing import Any, Dict
import os
# https://github.com/bojone/bert4keras/issues/231
os.environ["TF_KERAS"] = '1'
custom_objects: Dict[str, Any] = {}

from langma import corpus, embeddings, layers, macros, processors, tasks, utils
from langma.macros import config

custom_objects = layers.resigter_custom_layers(custom_objects)
