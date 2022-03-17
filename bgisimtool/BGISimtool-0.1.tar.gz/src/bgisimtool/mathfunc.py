# MIT License

# Copyright (c) 2018 Swann Levasseur

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from scipy.stats import chisquare
from scipy.stats import chi2
from scipy.optimize import curve_fit
from scipy.special import erf
import numpy as np
import copy as cp

# ==========================================
# Fit linear functions
# ==========================================


# 1st order linear function with no
def linear(x, a):
    return a * x


# fit a linear function
def fitLintoXY(x, y):
    popt, pcov = curve_fit(linear, x, y)
    perr = np.sqrt(np.diag(pcov))
    return [popt, perr]


# 1st order linear function
def linearOff(x, a, b):
    return (a * x) + b


# fit a linear function
def fitLinOfftoXY(x, y):
    popt, pcov = curve_fit(linearOff, x, y)
    perr = np.sqrt(np.diag(pcov))
    return [popt, perr]

# ==========================================
# Standard gaussian functions
# ==========================================


# gaussian function function
def gaussian(x, a, mu, sigma):
    return a * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))


# the cdf of a normal distribution
def cdf_gaussian(x, mu, sigma):
    return 0.5 * (1 + erf((x - mu) / (sigma * np.sqrt(2))))

# ---------------------
# fit
# ---------------------


# a function to fit a gaussian to a Histogram
def fit_gauss_to_hist(hist, yerr=None):
    """
    fit_gauss_to_hist, use scipy curve fit function to fit a gaussian function to the histogram provided
    Args:
        hist: a histogram object that contains _bin_center and _bin_content members.
        yerr: The error on the _bin_content if any.

    Returns:
        [popt, perr]:
        popt: The fit results with popt[0] the amplitude , popt[1] the mean and popt[2] the sigma.
        perr: The fit results with perr[0] the error on the amplitude, perr[1] the error on the mean
         and perr[2] the error on sigma.
    """
    # popt is the amplitude, mean and sigma
    # perr is the error on the aforementioned values
    popt, pcov = curve_fit(gaussian, hist._bin_center, hist._bin_content,
                           p0=[max(hist._bin_content), hist.mean, hist.stdev],
                           bounds=([0, -np.inf, 0], [np.inf, np.inf, np.inf]),
                           sigma=yerr)
    perr = np.sqrt(np.diag(pcov))
    return [popt, perr]

# ---------------------
# Get expected values
# ---------------------
def get_expected_bin_content_gaussian(bin_edge, exp_mean, exp_sigma, original_hist_intergral):
    expected = []
    max_bin_index = len(bin_edge)
    for i in range(max_bin_index-1):
        lower_value = cdf_gaussian(bin_edge[i], exp_mean, exp_sigma)
        upper_value = cdf_gaussian(bin_edge[i+1], exp_mean, exp_sigma)
        exp = (upper_value - lower_value) * original_hist_intergral
        expected.append(round(exp))
    return np.array(expected)


def process_vipm_histogram(vipm_histogram):
    # [1] Copy and update the given hist
    hist = cp.deepcopy(vipm_histogram)
    integral_before_changes = hist.integral
    hist.conditional_binning(content_limit=5)
    limits = (hist.mean - (5 * hist.stdev), hist.mean + (5 * hist.stdev))  # calc the limits at +- 5 sigma
    hist.reframe(limits)
    # [4] Get the error in y for the data
    yerr = np.sqrt(hist._bin_content)
    # [5] Fit to the requested model
    # Handle the possible error when the fit fail
    try:
        fit = fit_gauss_to_hist(hist, yerr=yerr)
        # [6] Get expected
        expec = get_expected_bin_content_gaussian(hist._bin_edge,
                                                  fit[0][1],
                                                  fit[0][2],
                                                  original_hist_intergral=integral_before_changes)
    except RuntimeError as e:
        # we just want to return null objects everywhere
        fit = None
        expec = None
        chi = None
        return hist, expec, fit, chi, False
    # no error, so we proceed
    # [7] Only keep bin with exp >= 5
    expec = hist.filter_by_expected(expec, 5)  # return the new exp list
    # [8] Do the chi2 test
    chi = chi2_test(hist._bin_content, expec, fit_parameter=3)
    # Return the result
    return hist, expec, fit, chi, True

# ==========================================
# chi2 test
# ==========================================
def get_ndf(observed_value, fit_parameter):
    ndf = 0
    for i in range(len(observed_value)):
        if observed_value[i] == 0 or observed_value[i] is np.nan:
            continue
        else:
            ndf += 1
    ndf = ndf - (fit_parameter + 1)
    return ndf

def get_chi_2_value(observed_value, expected_value):
    if not (len(observed_value) == len(expected_value)):
        raise ValueError('expected_value have a diferent size than observed_value')
    residuals = []
    for i in range(len(observed_value)):
        if observed_value[i] == 0 or observed_value[i] is np.nan:
            continue
        else:
            residuals.append(np.power((observed_value[i] - expected_value[i]) / np.sqrt(expected_value[i]), 2))
    chi = np.sum(residuals)
    return chi, np.array(residuals)


def chi2_test(observed_value, expected_value, fit_parameter=3):
    """ Based on the Pearson's chi-squared test.
        Calculate the raw chi2 and p value based on the number of fit parameters provided by the user"""

    if not (len(observed_value) == len(expected_value)):
        raise ValueError('expected_value have a diferent size than observed_value')
    # ---------------------------
    # CHI2
    # ---------------------------
    chi, residuals = get_chi_2_value(observed_value, expected_value)
    # ---------------------------
    # DoF
    # ---------------------------
    # get the number of degree of freedom ( number of non zero bins - (number of parameter in our fit function + 1) )
    ndf = get_ndf(observed_value, fit_parameter)
    # ---------------------------
    # get the P value
    # ---------------------------
    # use the survival function for that
    p_value = chi2.sf(chi, ndf)
    # return the result
    return chi, p_value, ndf, residuals
