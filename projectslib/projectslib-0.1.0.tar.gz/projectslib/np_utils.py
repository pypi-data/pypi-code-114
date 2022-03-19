import numpy as np


def unravel(flat_idxs, shape):
    return np.stack(np.unravel_index(flat_idxs, shape), axis=-1)
