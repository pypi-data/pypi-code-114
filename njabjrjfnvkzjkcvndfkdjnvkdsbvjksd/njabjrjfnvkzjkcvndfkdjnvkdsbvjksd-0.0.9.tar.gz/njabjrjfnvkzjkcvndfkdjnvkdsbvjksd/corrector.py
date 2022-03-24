# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:29:08 2022

@author: antoine
"""

import numpy as np
import gc

from tqdm import tqdm

from .utils import *
from .data_structurs import Triangle, Patern

class Corrector:
    def __init__(self, seqManager):
        self.seqManager = seqManager
        self.starsPosition = []
        self.paterns = []
        self.drifts = [[np.zeros((2))]]
        self.angles = [np.zeros((2))]
        
    def __len__(self):
        return len(self.seqManager)

        
    def getImgShape(self, idx = 0, idx_HDU = 0):
        return self.seqManager.getData(idx, idx_HDU).shape
    
    def getImg(self, idx = 0):
        return self.seqManager.getImg(idx)
    
    def getData(self, idx = 0, HDU = 0):
        return self.seqManager.getData(idx, HDU)
    
    def getReducedData(self, idx = 0, HDU = 0):
        return self.getImg(idx).getReducedData(HDU)
    
    def getInfo(self, idx = 0):
        return self.seqManager.getInfo(idx)
    
    def getHeader(self, idx = 0, HDU = 0):
        return self.seqManager.getHeader(idx)
    
    def histogram(self, idx = 0 , idx_HDU = 0):
        return self.seqManager.histogram(idx, idx_HDU)
    
    def getStarsListOfImg(self, idx):
        return self.starsPosition[idx]
    
    def detectStars(self):
        for i in range(len(self.seqManager)):
            img = self.seqManager.getImg(i)
            self.starsPosition.append(img.findStars(np.median(img.getData()) + np.std(img.getData())*0.8))
            del img
            gc.collect()
        
    def getImgCenter(self, idx_img = 0, idx_HDU = 0):
        return self.seqManager.getCenter(idx_img, idx_HDU)
        
    def findCloseststars(self, starList, idxOfStar):
        stars = np.zeros((5), dtype = int)
        distance = np.ones((5))*1000000
        
        stars[0] = idxOfStar
        distance[0] = 0
        
        for i,s in enumerate(starList):
            if i == idxOfStar:
                continue
            
            idx, distance = self.insertInArraySorted(distance,  Utils.dist(s, starList[idxOfStar]))

            if idx != -1:
                stars = Utils.insert(stars, idx, i)

        return stars
    
    def buildTriangles(self, stars):
        
        t1 = Triangle(stars[0], stars[1], stars[2])
        t2 = Triangle(stars[0], stars[1], stars[3])
        t3 = Triangle(stars[0], stars[2], stars[4])
        t4 = Triangle(stars[0], stars[2], stars[3])
        t5 = Triangle(stars[0], stars[2], stars[4])
        
        return t1, t2, t3, t4, t5
        
    def buildPatern(self, starsList):
        patern = []
        for i in range(len(starsList)): #iterate over all stars of an image
            stars = self.findCloseststars(starsList, i)
            t1, t2, t3, t4, t5 = self.buildTriangles(starsList[stars.astype(int)])
            patern.append(Patern(t1, t2, t3, t4, t5))
        return patern
    
    def buildPaterns(self):
        for i in self.starsPosition:
            self.paterns.append(self.buildPatern(i))
            
    def pop(self, idx = -1):
        self.seqManager.pop(idx)
        self.drifts.pop(idx)
        self.angles.pop(idx)
        self.paterns.pop(idx)
        self.starsPosition.pop(idx)
        
    
    def computeAngles(self, paternsOfImage1, paternsOfImage2):
        
        angle = []
        
        for i in paternsOfImage1:
            for j in paternsOfImage2:
                if i ==j:
                    angle.append(i.computeAngle(j))                
        return angle
    
    def computeDrift(self, paternsOfImage1, paternsOfImage2):
        
        drift = []
        for i in paternsOfImage1:
            for j in paternsOfImage2:
                
                if i == j:   
                    # print("pat 1: \n",i, "\npat 2: \n", j, "\ndist: ", i.computeDistance(j))
                    drift.append(i.computeDistance(j))
                    
        return drift
    
    def correctStarsFromRot(self, arrayToCorrect, idx, coefMultAngle = -1):
        
        angle = coefMultAngle*self.avgAng(idx)
        
        if np.isnan(angle):
            return
        
        center = self.getImgCenter(idx)
        
        stars = arrayToCorrect - center
        rot = np.asarray([[np.cos(angle), -np.sin(angle)],[np.sin(angle), np.cos(angle)]])
        return np.dot(stars, rot) + center
     
    def correctStarsFromRotTest(self, arrayToCorrect, idx, coefMultAngle = -1):
        
        arrayToCorrect = np.asarray(arrayToCorrect)
        
        angle = coefMultAngle*self.avgAng(idx)
        
        if np.isnan(angle):
            return
        
        newArry = np.column_stack((arrayToCorrect, np.ones((arrayToCorrect.shape[0]))))
        center = self.getImgCenter(idx)

        alpha = np.cos(angle)
        beta = np.sin(angle)
        
        rot = np.asarray([[alpha, beta, (1-alpha)*center[0] - beta*center[1]],[-beta, alpha, beta * center[0] + (1 - alpha)*center[1]]])
        
        return np.dot(rot, newArry.T).T
      
        
    def correctPaternFromRot(self, paterns, idx):
        for p in paterns:
            p.correctRot(-self.avgAng(idx), self.getImgCenter(idx))
        
    def imagesDrift(self):
        self.detectStars()
        self.buildPaterns()
    
        for i, p1 in enumerate(tqdm(self.paterns)): # iterate along images
            if i == 0:
                continue
            
            a = self.computeAngles(self.paterns[0], p1)
            self.angles.append(np.asarray(a))
 
            self.starsPosition[i] = self.correctStarsFromRotTest(self.starsPosition[i], i)
            self.correctPaternFromRot(p1, i)
           
            d = self.computeDrift(p1, self.paterns[0])
            self.drifts.append(d)
      
    def insertInArraySorted(self, arr, val):
        for i, e in enumerate(arr):
            if e > val:
                arr = Utils.insert(arr, i, val)
                return i, arr
        return -1, arr
    
    def medDrif(self, idx):
        return np.nanmedian(self.drifts[idx], axis = 0)
    def avgDrif(self, idx):
        return np.nanmean(self.drifts[idx], axis = 0)
    
    def medAng(self, idx):
        return np.nanmedian(self.angles[idx][np.logical_not(np.isnan(self.angles[idx]))])
    
    def avgAng(self, idx):
        return np.nanmean(self.angles[idx][np.logical_not(np.isnan(self.angles[idx]))])