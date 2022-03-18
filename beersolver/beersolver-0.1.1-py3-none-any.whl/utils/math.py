import logging

import numpy as np


from utils import log


def angle_between_vectors(vector_a: np.ndarray, vector_b: np.ndarray):
    return np.rad2deg(np.arccos(np.vdot(vector_a, vector_b) / np.vdot(np.linalg.norm(vector_a), np.linalg.norm(vector_b))))


def is_parallel(vector_a: np.ndarray, vector_b: np.ndarray):
    theta = angle_between_vectors(vector_a, vector_b)
    log.InternalLogger().log(f"Angle between {vector_a} and {vector_b} is {theta}", logging.DEBUG)

    if theta == 0.0 or theta == 180.0:
        return True
    else:
        return False
