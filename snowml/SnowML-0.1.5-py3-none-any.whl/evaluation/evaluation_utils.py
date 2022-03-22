import numpy as np


def find_best_threshold(fpr, tpr, thresholds):
    """
    Find best threshold from results of `metrics.roc_curve`.
    Threshold is considered best when it is the closest to (0,0) of the ROC curve.
    :param fpr: np.array / pd.Series of false positive rate values
    :param tpr: np.array / pd.Series of true positive rate values
    :param thresholds: cut off threshold range for predict probabilities
    :return: the best threshold which trying to minimize fpr and maximize tpr
    """

    dist = np.power(fpr, 2) + np.power(tpr - 1, 2)
    return thresholds[dist.argmin()]