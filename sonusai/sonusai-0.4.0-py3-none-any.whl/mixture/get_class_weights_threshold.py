from typing import List

from sonusai import SonusAIError
from sonusai import logger


def get_class_weights_threshold(mixdb: dict) -> List[float]:
    class_weights_threshold = mixdb['class_weights_threshold']
    if not isinstance(class_weights_threshold, list):
        class_weights_threshold = [class_weights_threshold] * mixdb['num_classes']
    if len(class_weights_threshold) != mixdb['num_classes']:
        logger.error(f'invalid class_weights_threshold length: {len(class_weights_threshold)}')
        raise SonusAIError
    return class_weights_threshold
