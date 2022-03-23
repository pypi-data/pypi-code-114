import pandas as pd
import numpy as np
import scipy.stats as stats
#Comment Azmi 
class Stats_BS():
    def __init__(self):
        super().__init__()  
    def make_stats(n):
        return stats.kurtosis(n, nan_policy = 'omit'), stats.gmean(n),stats.skew(n, nan_policy = 'omit')

 