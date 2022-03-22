import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

from scipy.special import loggamma

from .beta import Beta
from .gamma import Gamma
from .normal import Normal, NormalGamma


def simulation(*args, size=10000):
    if len(args) < 2:
        raise ValueError('must provide at least two modeled distributions.')
        
    samples = np.column_stack([model.sample(size) for model in args])
    winners = samples.argmax(axis=1)

    return samples, winners

def probability_to_be_better(samples):
    n_variants = samples.shape[1]
    winner_array = samples.argmax(axis=1)
    
    best_proba = []
    for i in range(n_variants):
        wins = (winner_array == i)
        best_proba.append(sum(wins) / len(wins))

    return best_proba
    

def expected_loss(samples, winners):
    n_variants = samples.shape[1]
    win_array =np.array([samples[row, win_idx] for row,win_idx in enumerate(winners)])

    e_loss = []
    for variant_id in range(n_variants):
        losing_vec = samples[winners != variant_id, variant_id]
        win_vec = win_array[winners != variant_id]

        mean_loss =  np.subtract(win_vec, losing_vec).sum() / samples.shape[0]

        e_loss.append(mean_loss)

    return e_loss