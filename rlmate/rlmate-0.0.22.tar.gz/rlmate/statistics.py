import numpy as np
from scipy.stats import t
from scipy.stats import norm

def binomial_variance(num0, num1, val0, val1):
    n = num0 + num1
    x = num0/n*val0 + num1/n*val1
    return num0/(n-1)*np.power((val0-x),2) + num1/(n-1)*np.power((val1-x), 2)

def construct_confidence_interval_length(values, kappa = 0.05):
    var = np.var(values, ddof=1)
    std_dev = np.sqrt(var)
    n = len(values)
    t_stat =  t(df=n - 1).ppf((kappa / 2, 1 - kappa / 2))[-1]
    
    return 2 * (t_stat * std_dev / np.sqrt(n))

def construct_confidence_interval(values, kappa = 0.05):
    var = np.var(values, ddof=1)
    mean = np.mean(values)
    std_dev = np.sqrt(var)
    n = len(values)
    t_stat =  t(df=n - 1).ppf((kappa / 2, 1 - kappa / 2))[-1]
    interval = [mean-t_stat*std_dev/np.sqrt(n),mean+t_stat*std_dev/np.sqrt(n)]

    return interval

def construct_binomial_confidence_interval_length(num0, num1, val0 = 0, val1 = 1, kappa = 0.05):
    var = binomial_variance(num0, num1, val0, val1)
    n = num0 + num1
    std_dev = np.sqrt(var)
    t_stat =  norm.ppf((kappa / 2, 1 - kappa / 2))[-1]
    
    return 2 * (t_stat * std_dev / np.sqrt(n))

def construct_binomial_confidence_interval(num0, num1, val0 = 0, val1 = 1, kappa = 0.05):
    var = binomial_variance(num0, num1, val0, val1)
    n = num0 + num1
    mean = num0/n*val0 + num1/n*val1
    std_dev = np.sqrt(var)
    t_stat =  norm.ppf((kappa / 2, 1 - kappa / 2))[-1]
    interval = [mean-t_stat*std_dev/np.sqrt(n),mean+t_stat*std_dev/np.sqrt(n)]
    
    return interval

