# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:29:07 2022

@author: antoine
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arrow
from matplotlib.backend_bases import MouseButton
import cv2

class Utils:
    def patToArw(pat):
        s1 = pat.t1.s1
        s2 = pat.t1.s2
        s3 = pat.t1.s3
        s4 = pat.t2.s3
        
        d2 = s2 - s1
        d3 = s3 - s1
        d4 = s4 - s1
        c = [random.random(), random.random(), random.random()]
        a2 = Arrow(s1[0], s1[1], d2[0], d2[1], color=c)
        a3 = Arrow(s1[0], s1[1], d3[0], d3[1], color=c)
        a4 = Arrow(s1[0], s1[1], d4[0], d4[1], color=c)
        
        return a2, a3, a4

    def imshowpatern(img, paterns):
        fig,ax = plt.subplots(1)
        for i in paterns:
            a1, a2, a3 = Utils.patToArw(i)
            ax.add_patch(a1)
            ax.add_patch(a2)
            ax.add_patch(a3)
            
        ax.imshow(img, cmap="Greys", vmin = np.mean(img)*0.5, vmax = np.mean(img)/0.5)
        
    def polarRot(starArray, shape, angle):
        
        if np.isnan(angle):
            print('angle is Nan')
            return
        
        center = ((np.asarray(shape) / 2) + 0.5).astype(int)
       
        stars = starArray - center
        rot = np.asarray([[np.cos(angle), -np.sin(angle)],[np.sin(angle), np.cos(angle)]])
        return np.dot(stars, rot) + center

    def dist(star1, star2 = [0,0]):
        return np.sum((np.asarray(star2) - np.asarray(star1))**2)**0.5
    
    def insert(arr, idx, val):
        arr = np.insert(arr, idx, val)
        return np.delete(arr, -1)
    
    def isPresent(lis, val):
        for i in lis:
            if i == val:
                return True
        return False
    
    def imshowstar(img, stars, angle = None, drift = np.zeros((2)), isImageToMove = True):
        fig,ax = plt.subplots(1)
        
        if angle != None and angle != 0.0:
            if isImageToMove:
                img = Utils.rotate_image(img, Utils.rtod(angle))
            else:
                stars = Utils.polarRot(stars, img.shape, angle)
                
        if (drift != np.zeros((2))).all():
            if isImageToMove:
                img = np.roll(img, -int(drift[0]+0.5), axis=1)
                img = np.roll(img, -int(drift[1]+0.5), axis=0)
            else:
                stars -= drift
                
        for i in stars:
            c = Circle(i, radius = 50, fill=False)
            ax.add_patch(c)
            
        ax.imshow(img, cmap="Greys", vmin = np.nanmean(img)*0.5, vmax = np.nanmean(img)/0.5)

    def getPosFromImage(event, posList, isClose):
        if event.button is MouseButton.LEFT:
           posList.append(np.asarray([event.xdata, event.ydata]))
           print("Position x: ", posList[-1][0], ' y: ', posList[-1][1])
           
        if event.button is MouseButton.RIGHT:
            isClose[0] = True
            plt.close()
    
    def add(img1, img2):
        fig,ax = plt.subplots(1)
        ax.imshow((img1 + img2)/2, cmap="Greys", vmin = np.mean((img1 + img2)/2)*0.5, vmax = np.mean((img1 + img2)/2)/0.5)
        plt.show()
            
    def centred(xy, img, eps):
        for i in range(len(xy)):
            x = int(xy[i][0] + 0.5)
            y = int(xy[i][1] + 0.5)
            cent = img[y - eps : y + eps, x - eps : x + eps]
            # Utils.imshow(cent)
            pos = np.flip(np.asarray(np.where(cent == np.max(cent)))[:,0].reshape((2)))
            xy[i] = np.asarray(xy[i]) + (pos - eps)
        return xy

    def imshow(img):
        plt.figure()
        plt.imshow(img, cmap='Greys', vmin = np.median(img[img>0])*0.5, vmax = np.median(img[img>0]) / 0.5)
        
    def imshowap(img, r, pos):
       
        img = img[int((pos[1] - r)+0.5): int((pos[1] + r)+0.5), int((pos[0] - r) + 0.5) : int((pos[0] + r) + 0.5)]
        c = Circle(np.asarray(img.shape)/2, radius = 50, fill=False)
        fig,ax = plt.subplots(1)
        ax.add_patch(c)
        ax.imshow(img, cmap='Greys', vmin = np.median(img)*0.5, vmax = np.median(img) / 0.5)
        return np.sum(img)
    
    
    def binn(by, file):
        pointer = 0
        
        newSize = int(file.shape[0] / by)
        limit = newSize * by
        
        if len(file.shape) >1:
            newData = np.zeros((newSize, file.shape[1]), dtype=file.dtype)
        else:
             newData = np.zeros((newSize), dtype=file.dtype)
        
        while pointer < limit:
            
            for i in range(by):
                if len(file.shape) >1:
                    newData[int(pointer/by), :] += file[i + pointer, :]
                else :
                    newData[int(pointer/by)] += file[i + pointer]
                    
            pointer += by
    
        return newData / by    
    
    def rescalMulti(asts, stars):
        mmax = np.nanmax(asts)
        mmin = np.nanmin(asts)
        offset = []
        for i in range(stars.shape[1]):
            mmax2 = np.nanmax(stars[:,i])
            mmin2 = np.nanmin(stars[:,i])
                
            offset.append(np.min([mmax - mmin2, mmin - mmax2]) - 0.01)
        
        return np.asarray(offset)
    
    def rotate_image(image, angle):
        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        return result
    
    
    def rtod(r):
        return r*180 / np.pi
    
    def mad(tab):
        """Median std"""
        med = np.median(tab)
        return np.sqrt(np.median((tab - med)**2))
    
    def hist(tab):
        hist = np.zeros((2**16))
        for i in range(tab.shape[0]):
            for j in range(tab.shape[1]):
                hist[tab[i,j]] += 1
        
        return hist
    
    def histCum(tab):
        hist = Utils.hist(tab)
        hc = np.zeros((2**16))
        for i in range(hist.shape[0]):
           if i == 0: 
               hc[0] = hist[0]
           else:
               hc[i] = hc[i-1] + hist[i]
        
        return hc