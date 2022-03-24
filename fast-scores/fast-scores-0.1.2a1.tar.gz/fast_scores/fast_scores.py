"""Calculate fast_scores."""
from typing import List

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from logzero import logger

from fast_scores.cos_matrix2 import cos_matrix2
from fast_scores.gen_model import gen_model


# fmt: off
def fast_scores(
        text1: List[str],
        text2: List[str],
        model: TfidfVectorizer = None,
        dot: bool = True,
) -> np.ndarray:
    # fmt: on
    """Calculate fast_scores.

    Args:
        text1: chinese text
        text2: chinese text

    Returns:
        correlation matrix (float)
    """
    # logger.debug(" entry ")

    # create model on the fly
    if model is None:
        logger.info("No model provided, creating one on the fly")
        try:
            # model = TfidfVectorizer().fit(text1 + text2)
            model = gen_model(text1 + text2)
        except Exception as e:
            logger.error(e)
            raise SystemExit(1) from e
        logger.info("Done creating model")
        # shake 10000x10000 ~7s-16s

    vec1 = model.transform(text1)  # scipy.sparse.csr.csr_matrix
    vec2 = model.transform(text2)

    # supposed to be much faster
    if dot:
        return vec1.dot(vec2.T).toarray().T
    # shake 10000x11000 41.1 s ± 15.5 s
    # shake 5000x5100 11s
    # shake 2000x2100 3.7s
    # shake 1000x1100 2.1s
    # shake 10000x10100 3min 1min 13s
    # comfort zone length: j = math.sqrt(psutil.virtual_memory().available/64)
    # estimated time: j / 1000 * 2 s

    return cos_matrix2(vec1.toarray(), vec2.toarray()).T
    # shake 1000x1100 11s 21s
    # shake 2000x2100 45s
    # shake 10000x10000
