"""
    distance scoring methods

    methods include
    ------------------------------------
    1. adjusted_cosine
    2. score_method_handler
"""
from scipy import spatial
import numpy as np

def adjusted_cosine(base_vector, comp_vector):
    """finds indices in entity_vector that equal, removes in both vectors and applies cosine

    Args:
        base_vector (list): base vector
        comp_vector (list): comparison vector

    Returns:
        float: adjusted cosine score
    """
    if isinstance(base_vector, np.ndarray):
        base_vector = base_vector.tolist()

    if isinstance(comp_vector, np.ndarray):
        comp_vector = comp_vector.tolist()

    indices = [
        i for i, x in enumerate(base_vector) if x == 0
    ]  # must be from joblisting

    indices = sorted(indices, reverse=True)

    for idx in indices:
        comp_vector.pop(idx)

    for idx in indices:
        base_vector.pop(idx)

    return 1 - spatial.distance.cosine(base_vector, comp_vector)

def score_method_handler(base_vector: list, comp_vector: list, scorer_types: list) -> dict:
    """scorer method handler

    Args:
        base_vector (list): base vector
        comp_vector (list): comparison vector
        scorer_types (list): scorer types to run scoring for

    Raises:
        TypeError: _description_

    Returns:
        dict: scores for given vectors
    """
    scores = {}

    if "simple_cosine" in scorer_types:

        score = 1 - spatial.distance.cosine(base_vector, comp_vector)
        scores["simple_cosine"] = score

    if "adjusted_cosine" in scorer_types:

        scores["adjusted_cosine"] = adjusted_cosine(base_vector, comp_vector)

    if "simple_euclidean" in scorer_types:

        # score = np.linalg.norm(np.asarray(base_1)-np.asarray(comp_1))#this is theoratically faster function
        score = 1 / (
            1 + spatial.distance.euclidean(base_vector, comp_vector)
        )  # this is a slower function, should actually use np sqrt
        scores["simple_euclidean"] = score

    if len(scores.keys()) == 0:
        raise TypeError(f"None of `scorer_types` == {scorer_types} are currently supported")

    return scores
