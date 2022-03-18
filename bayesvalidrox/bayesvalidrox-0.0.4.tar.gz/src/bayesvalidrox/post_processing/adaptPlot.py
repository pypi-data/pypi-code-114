#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:46:24 2020

@author: farid
"""

import numpy as np
import os
from sklearn.metrics import mean_squared_error, r2_score
from itertools import cycle
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 24})
plt.rc('figure', figsize = (24, 16))
plt.rc('font', family='serif', serif='Arial')
plt.rc('axes', grid = True)
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=24)
plt.rc('ytick', labelsize=24)
plt.rc('axes', labelsize=24)
plt.rc('axes', linewidth=2)
plt.rc('axes', grid=True)
plt.rc('grid', linestyle="-")
plt.rc('savefig', dpi=1000)

def adaptPlot(PCEModel, Y_Val, Y_PC_Val, Y_PC_Val_std, x_values=[], plotED=False, SaveFig=True):
    
    NrofSamples = PCEModel.ExpDesign.n_new_samples
    initNSamples = PCEModel.ExpDesign.n_init_samples
    itrNr = 1 + (PCEModel.ExpDesign.X.shape[0] - initNSamples)//NrofSamples

    oldEDY =  PCEModel.ExpDesign.Y
    
    if SaveFig:
        newpath = (r'adaptivePlots')
        if not os.path.exists(newpath): os.makedirs(newpath)
        
        # create a PdfPages object
        pdf = PdfPages('./'+newpath+'/Model_vs_PCEModel'+'_itr_'+str(itrNr)+'.pdf')

    # List of markers and colors
    color = cycle((['b', 'g', 'r', 'y', 'k']))
    marker = cycle(('x', 'd', '+', 'o', '*')) 
    
    OutNames = list(Y_Val.keys())
    x_axis = 'Time [s]'
    if len(OutNames) == 1: OutNames.insert(0, x_axis)
    try:
        x_values =  Y_Val[OutNames[0]]
    except:
        x_values =  x_values
    
    fig = plt.figure(figsize=(24, 16))
    
    # Plot the model vs PCE model
    for keyIdx, key in enumerate(OutNames[1:]):

        Y_PC_Val_ = Y_PC_Val[key]
        Y_PC_Val_std_ = Y_PC_Val_std[key]
        Y_Val_ = Y_Val[key]
        old_EDY = oldEDY[key]
        
        for idx in range(NrofSamples):
            Color = next(color)
            Marker = next(marker)
            
            plt.plot(x_values, Y_Val_[idx,:], color=Color, marker=Marker, lw=2.0, label='$Y_{%s}^{M}$'%(idx+itrNr))
            
            plt.plot(x_values, Y_PC_Val_[idx,:], color=Color, marker=Marker, lw=2.0, linestyle='--', label='$Y_{%s}^{PCE}$'%(idx+itrNr))
            plt.fill_between(x_values, Y_PC_Val_[idx,:]-1.96*Y_PC_Val_std_[idx,:], 
                              Y_PC_Val_[idx,:]+1.96*Y_PC_Val_std_[idx,:], color=Color,alpha=0.15)
            
            if plotED:
                for output in old_EDY:
                    plt.plot(x_values, output, color='grey', alpha=0.1)
            
        # Calculate the RMSE
        RMSE = mean_squared_error(Y_PC_Val_, Y_Val_, squared=False)
        R2 = r2_score(Y_PC_Val_.reshape(-1,1), Y_Val_.reshape(-1,1))
        
        plt.ylabel(key)
        plt.xlabel(x_axis)
        plt.title(key)
        
        ax = fig.axes[0]
        ax.legend(loc='best', frameon=True)
        fig.canvas.draw()
        ax.text(0.65, 0.85, 'RMSE = '+ str(round(RMSE, 3)) + '\n' + r'$R^2$ = '+ str(round(R2, 3)),
                transform=ax.transAxes, color='black', bbox=dict(facecolor='none', edgecolor='black', 
                                         boxstyle='round,pad=1'))
        
        plt.grid()
        
        if SaveFig:
            # save the current figure
            pdf.savefig(fig, bbox_inches='tight')
            
            # Destroy the current plot
            plt.clf()
        
    pdf.close()