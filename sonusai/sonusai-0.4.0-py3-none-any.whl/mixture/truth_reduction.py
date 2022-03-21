import numpy as np

from sonusai import SonusAIError
from sonusai import logger


def truth_reduction(x: np.ndarray, func: str) -> np.ndarray:
    if func == 'max':
        return np.max(x, axis=0)

    if func == 'mean':
        return np.mean(x, axis=0)

    logger.error(f'Invalid truth reduction function: {func}')
    raise SonusAIError
