r"""Define cmat2aset.

Refer to pypi radiobee-aligner\radiobee\gradiobee.py
    aset = gen_aset(pset, src_len, tgt_len)
"""
# pylint: disable=invalid-name

from typing import List, Tuple, Union
import numpy as np

from logzero import logger

from cmat2aset.gen_pset import gen_pset
from cmat2aset.gen_aset import gen_aset

# from cmat2aset.gen_aset import gen_aset


def cmat2aset(
    cmat: Union[np.ndarray, List[List]],
    eps: float = 10,
    min_samples: int = 6,
) -> Union[
    np.ndarray, List[Tuple[Union[int, str], Union[int, str], Union[float, str]]]
]:
    """Convert cmat to aset."""
    try:
        cmat = np.array(cmat)
    except Exception as e:
        logger.exception(e)
        raise

    if np.array(cmat).ndim != 2:
        raise Exception("Expected a 2d array...")

    for min_s in range(min_samples):
        logger.info(" min_samples, using %s", min_samples - min_s)
        try:
            pset = gen_pset(
                cmat,
                eps=eps,
                min_samples=min_samples - min_s,
                delta=7,
            )
            break
        except ValueError:
            logger.info(" decrease min_samples by %s", min_s + 1)
            continue
        except Exception as e:
            logger.error(e)
            continue
    else:
        # break should happen above when min_samples = 2
        raise Exception("bummer, this shouldn't happen, probably another bug")

    src_len, tgt_len = cmat.shape
    aset = gen_aset(pset, src_len, tgt_len)

    # _ = [(int(elm0), int(elm1), float(elm2) if isinstance(elm2, float) else str(elm2)) for elm0, elm1, elm2 in aset]
    _ = []
    for elm0, elm1, elm2 in aset:
        _.append(
            (
                int(elm0) if isinstance(elm0, (int, float)) else elm0,
                int(elm1) if isinstance(elm1, (int, float)) else elm1,
                round(elm2, 2) if isinstance(elm2, float) else elm2,
            )
        )

    # return np.array(aset)
    return _
