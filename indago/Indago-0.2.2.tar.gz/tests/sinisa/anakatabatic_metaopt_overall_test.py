# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:58:25 2019
Anakatabatic overall test
@author: Sinisa
"""

import sys
sys.path.append('..\..')
from indago.benchmarks import CEC2014
from indago import PSO
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import time
from scipy.interpolate import interp1d


# cec funs optimization parameters
cecD = 10
cecmaxit = 100 * cecD
cecruns = 960 # 1000+ would be safe
CEC = CEC2014(cecD)

# parallel execution
NP = 12 # number of parallel processes
assert cecruns % NP == 0

# testing variant
VARIANT = 'Vanilla'
#VARIANT = 'TVAC'

##############################################################################

# load base results
FITmedbyf_base = np.loadtxt('anakatabatic_metaopt_overall_test_base_' + VARIANT + '.txt')
FITmedbyf_base = FITmedbyf_base[[10, 20, 50].index(cecD), :]

def computecec(cec, pso, runs):
    np.random.seed()
    FITmedbyf = []
    for f in cec.functions:
        pso.evaluation_function = f
        FITraw = np.zeros(runs) * np.nan
        for r in range(runs):
            FITraw[r] = pso.optimize().f
        FITmedbyf.append(np.median(FITraw))
    return np.array(FITmedbyf)
    
def metagoaleval(akb_model, f_start, f_stop, pool, setup, computecec=computecec):
        
    D, maxit, runs, cec, pso = setup
        
    pso.dimensions = D
    pso.iterations = maxit
    pso.lb = -100
    pso.ub = 100
    
    pso.eval_fail_behavior = 'ignore'
    
    # do all funs with default w
    FITmedbyf_base = np.median(pool.starmap(computecec,
                        [(cec, pso, cecruns//NP) for _ in range(NP)]), axis=0)
    #print(FITmedbyf_base)
    
    # do all funs with anakatabatic w
    pso.params['inertia'] = 'anakatabatic'
    if akb_model:
        pso.params['akb_model'] = akb_model
    else:
        pso.params['akb_fun_start'] = f_start
        pso.params['akb_fun_stop'] = f_stop
    FITmedbyf_akb = np.median(pool.starmap(computecec,
                        [(cec, pso, cecruns//NP) for _ in range(NP)]), axis=0)
    
    # COMPUTE LOG-SCORE
    score = np.nanmean(np.log10(FITmedbyf_akb/FITmedbyf_base))
    print(f'omega [oom]: {-score:6.3f}')
        
    # COMPUTE ALPHA-SCORE
    score = np.nanmean(2 * (FITmedbyf_base - FITmedbyf_akb)/(FITmedbyf_base + FITmedbyf_akb))
    print(f'alpha [-]: {score:6.3f}')   

##############################################################################

### Anakatabatic Vanilla

# akb_model = 'Languid'
# # omega [oom]: 0.042, 0.139, ???
# # alpha: 0.092, 0.197, ???
    
# akb_model = 'FlyingStork'
# # omega [oom]: 0.043, 0.118, ???
# # alpha: 0.098, 0.188, ???

# akb_model = 'MessyTie'
# # omega [oom]: -0.173, ???, ???
# # alpha: -0.338, ???, ???

# 'med'
w_start = [-0.32, -0.06, -0.16, -0.63, 0.31]
w_stop = [0.16, 0.21, 0.42, -0.55, 0.03]
# omega [oom]: ???, ???, ???
# alpha: ???, ???, ???

# # '2med'
# w_start = np.array([-0.32, -0.06, -0.16, -0.63, 0.31]) * 2
# w_stop = np.array([0.16, 0.21, 0.42, -0.55, 0.03]) * 2
# # omega [oom]: ???, ???, ???
# # alpha: ???, ???, ???

# # '3med'
# w_start = np.array([-0.32, -0.06, -0.16, -0.63, 0.31]) * 3
# w_stop = np.array([0.16, 0.21, 0.42, -0.55, 0.03]) * 3
# # omega [oom]: ???, ???, ???
# # alpha: ???, ???, ???
	

""" MAIN STUFF """

# akb_model, f_start, f_stop = None, None, None
try:            # if akb_model exists, akb functions are not needed
    akb_model  
    f_start, f_stop = None, None
except:         # if akb_model does not exist, create akb functions
    akb_model = None
    Th = np.linspace(np.pi/4, 5*np.pi/4, 5)
    f_start = interp1d(Th, w_start, kind='linear')
    f_stop = interp1d(Th, w_stop, kind='linear')


if __name__ == '__main__': # multiprocessing needs this maybe

    print(f'variant: {VARIANT}')
    print(f'model: {akb_model}') 
    print(f'D = {cecD}; cecruns = {cecruns}')
    pool = Pool(NP)
    pso = PSO()
    pso.method = VARIANT
    setup = [cecD, cecmaxit, cecruns, CEC, pso]
    startt = time.time()
    score = metagoaleval(akb_model, f_start, f_stop, pool, setup, computecec=computecec)
    pool.close()
    stopt = time.time()
    print(f'elapsed time [hr]: {(stopt-startt)/3600:.3f}') 
    
    """
    # plot
    THplot = np.linspace(np.pi/4, 5*np.pi/4, 200)
    plt.plot(THplot, f_start(THplot), 'g', label='akb_fun_start')
    plt.plot(THplot, f_stop(THplot), 'r', label='akb_fun_stop')
    plt.axhline(color='magenta', ls=':')
    plt.axvline(2*np.pi/4, color='magenta', ls=':')
    plt.axvline(4*np.pi/4, color='magenta', ls=':')
    plt.axis([np.pi/4, 5*np.pi/4, -2, 3])
    plt.xlabel(r'$\theta_i$')
    plt.ylabel('$w_i$')
    plt.title(f'{akb_model}')
    plt.legend()
    plt.show()
    """

