"""Define ezbee."""
from typing import List

from logzero import logger


def ezbee(
    text1: List[str],
    text2: List[str],
    eps: float = 10,
    min_samples: int = 6,
) -> List:
    """Define."""
    del text1
    del text2
    logger.debug(" entry %s", [eps, min_samples])

    return []
