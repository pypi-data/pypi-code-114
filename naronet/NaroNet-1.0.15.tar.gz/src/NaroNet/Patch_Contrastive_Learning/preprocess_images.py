"""
This module normalizes the cohort based on the mean and standard deviation.
"""

import os
import numpy as np
import random
from tqdm import tqdm
import csv
from NaroNet.utils.parallel_process import parallel_process
import NaroNet.utils.utilz as utilz
from skimage import io
import time
import cv2 as cv
import gc

def Mean_std_experiment(obj, base_path,image_paths,Channels):    
    ''' 
    Obtain mean and standard deviation from the cohort
    base_path: (string) that specifies the directory where the experiment is carried out.
    images_paths: (list of strings) that specifies the names of the files executed.
    Channels: (vector of int) channels that should be included in the experiment.    
    '''
    
    # Read slide by slide
    for n_im in tqdm(range(len(image_paths)),ascii=True,desc='Calculate Mean and Standard deviation'): 
        
        # Load Image
        image = obj.load_image(n_im)

        # Reduce image size if it is too large
        max_num_pix = 5000000
        max_num_pix_dim = int(max_num_pix**0.5)
        im_s = image.shape
        if im_s[0]*im_s[1]>max_num_pix:
            image = image[0:im_s[0]:int(im_s[0]/max_num_pix_dim),0:im_s[1]:int(im_s[1]/max_num_pix_dim),:]
        
        # To concatenate image information we sum the histograms of several images.
        if n_im==0:
            minImage = image.min(tuple(range(len(image.shape)-1)))
            minImage = [m*10 if m<0 else m/10 for m in minImage]
            maxImage = image.max(tuple(range(len(image.shape)-1)))
            maxImage = [m/10 if m<0 else m*10 for m in maxImage]
            Global_hist = [list(np.histogram(np.concatenate((image[:,:,i].flatten(),np.arange(minImage[i],maxImage[i],(maxImage[i]-minImage[i])/10000))),range=(minImage[i],maxImage[i]),bins=10000)) for i in range(image.shape[-1])]                                    
        else:
            Local_hist = [list(np.histogram(np.concatenate((image[:,:,i].flatten(),np.arange(minImage[i],maxImage[i],(maxImage[i]-minImage[i])/10000))),range=(minImage[i],maxImage[i]),bins=10000)) for i in range(image.shape[-1])]                                    
            for n_g_h, g_h in enumerate(Global_hist):
                g_h[0] += Local_hist[n_g_h][0]      

        del image 
        gc.collect(0)
        gc.collect(1)
        gc.collect(2)

    # Calculate Mean
    mean = []    
    for g_h in Global_hist:
        hist_WA = []
        den = 0
        num = 0
        for g_n, g_h_h in enumerate(g_h[0]):
            den+=(g_h_h-(n_im+1)+1e-16)
            num+=g_h[1][g_n]*(g_h_h-(n_im+1)+1e-16)
        mean.append(num/den)
    
    # Calculate Standard deviation
    std = []
    for hn, g_h in enumerate(Global_hist):
        hist_WA = []
        den = 0
        num = 0
        for g_n, g_h_h in enumerate(g_h[0]):
            den+=(g_h_h-(n_im+1)+1e-16)
            num+=((g_h[1][g_n]-mean[hn])**2)*(g_h_h-(n_im+1)+1e-16)
        std.append((num/den)**0.5)

    # Save mean and std to file
    with open(base_path[:-7]+'Experiment_Stats.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(mean)
        writer.writerow(std)

    return np.array(mean, dtype=np.float32), np.array(std, dtype=np.float32)
