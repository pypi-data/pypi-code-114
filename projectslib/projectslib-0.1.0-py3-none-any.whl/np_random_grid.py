import numpy as np
from . import np_utils


def random_grid_point(pvals, samples=1, rng=np.random.default_rng()):
    num_points = np.product(pvals.shape)
    flat_points = rng.choice(num_points, size=samples, p=pvals.flatten())
    return np_utils.unravel(flat_points, pvals.shape)


def random_rectangle(shape, samples=1, rng=np.random.default_rng()):
    num_points = np.product(shape)
    # Samples x Shape
    corners1 = np_utils.unravel(rng.integers(num_points, size=samples), shape)
    corners2 = np_utils.unravel(rng.integers(num_points, size=samples), shape)
    return np.maximum(corners1, corners2), np.minimum(corners1, corners2)
