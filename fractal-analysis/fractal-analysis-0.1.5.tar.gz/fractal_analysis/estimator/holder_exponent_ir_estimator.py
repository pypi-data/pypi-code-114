from typing import Union, List

import numpy as np
import pandas as pd
import math


class HolderExponentIrEstimator:
    """
        Source paper: Bardet, Jean-Marc & Surgailis, Donatas, 2013.
                      "Nonparametric estimation of the local Hurst function of multifractional Gaussian processes,"
                      Stochastic Processes and their Applications, Elsevier, vol. 123(3), pages 1004-1045.
        Original Matlab code source: http://samm.univ-paris1.fr/Sofwares-Logiciels
                                     Software for estimating the Hurst function H of a Multifractional Brownian Motion:
                                     Quadratic Variation estimator and IR estimator
    """

    def __init__(self, mbm_series: Union[List, np.ndarray, pd.Series], alpha: float):
        """
            mbm_series: multifractional Brownian motion series
            alpha: decide how many observations on mbm_series is used to estimate a point of the holder exponent;
                   small alpha means more observations are used for a single point and therefore the variance is small.
        """
        self.mbm_series = np.array(mbm_series)
        self.alpha = alpha
        if not (0 < self.alpha < 1):
            raise ValueError(f'Alpha must be in range (0, 1).')
        self.n = len(self.mbm_series)

    @staticmethod
    def _ismember(a, b):
        bind = {}
        for i, elt in enumerate(b):
            if elt not in bind:
                bind[elt] = i
        return [bind.get(itm, None) for itm in a]  # None can be replaced by any other "not in b" value

    def _neighborhood(self, t: int):
        """
            The function $\mathcal{V}_{n,\alpha}(t)$ in Sec 2.1 of the source paper:
                      Bardet, Jean-Marc & Surgailis, Donatas, 2013.
                      "Nonparametric estimation of the local Hurst function of multifractional Gaussian processes,"
                      Stochastic Processes and their Applications, Elsevier, vol. 123(3), pages 1004-1045.
        """
        n_to_1_minus_alpha = self.n ** (1 - self.alpha)
        k_min = max(0.0, math.ceil(t - n_to_1_minus_alpha))
        k_max = min(float(self.n - 3 - 2), math.floor(t + n_to_1_minus_alpha))
        return np.arange(start=k_min, stop=k_max + 1, step=1, dtype=int)

    @staticmethod
    def _hest_ir(R, p: int):
        """
            Equivalent to matlab function HestIR(R,p) in the source code:
                        http://samm.univ-paris1.fr/Sofwares-Logiciels
                        Software for estimating the Hurst function H of a Multifractional Brownian Motion:
                        Quadratic Variation estimator and IR estimator
            This is $\Lambda_2^{-1}(H)$ (inverse function of eq. 2.5) in the paper:
                        Bardet, Jean-Marc & Surgailis, Donatas, 2013.
                        "Nonparametric estimation of the local Hurst function of multifractional Gaussian processes,"
                        Stochastic Processes and their Applications, Elsevier, vol. 123(3), pages 1004-1045.
        """
        start = 0.0001
        stop = 0.9999
        step = 0.0001
        H = np.arange(start, stop + step, step)
        if p == 1:
            r = 2 ** (2 * H - 1) - 1
        elif p == 2:
            r = (-3 ** (2 * H) + 2 ** (2 * H + 2) - 7) / (8 - 2 ** (2 * H + 1))
        else:
            raise ValueError('p is the order of the IR statistic; only takes 1 or 2.')
        lam = 1 / np.pi * np.arccos(-r) + np.sqrt(1 - r ** 2) / (np.pi * (1 - r)) * np.log(2 / (r + 1))
        return sum(R > i for i in lam) / 10000

    @property
    def holder_exponents(self):
        mgn_series = self.mbm_series[1:] - self.mbm_series[:-1]
        ir_estimates = []
        for t in range(self.n):
            k = self._neighborhood(t=t)
            R2 = np.mean(np.abs(mgn_series[3 + k] - mgn_series[1 + k]) / (
                    np.abs(mgn_series[3 + k] - mgn_series[2 + k]) + np.abs(mgn_series[2 + k] - mgn_series[1 + k])))
            ir_estimates.append(self._hest_ir(R=R2, p=2))
        return np.array(ir_estimates)
