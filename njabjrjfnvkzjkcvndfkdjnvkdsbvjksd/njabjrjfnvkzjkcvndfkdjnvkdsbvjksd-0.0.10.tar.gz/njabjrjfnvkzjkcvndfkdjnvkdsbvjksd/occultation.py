# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:35:12 2022

@author: antoine
"""

import numpy as np

from .corrector import *
from .data_structurs import SeqManager, Appertur

from astropy.time import Time


class Occult(Corrector):
    def __init__(self, seq):
        super().__init__(SeqManager(seq))
        print(self.getHeader())
        self.key = str(input("ENTER THE KEY OF A TIME REF WITH | SEPARATOR IF NEEDED (exemple JD | jd or DATE-OBS | isot. Refere to Time.FORMATS from astropy.time): "))
        
        self.apperturs = []
        self.refStars = []
        self.objectOfInterst = []
        self.results = []
    
    
    def start(self, r, ri, re, correct = False):
        print("SELECT REFERENCES STARS")
        self.selectAp(r, self.refStars)
        print("SELECT STAR OF INTERREST")
        self.selectAp(r, self.objectOfInterst)
        self.objectOfInterst = Utils.centred(self.objectOfInterst, self.getImg().getData(), r)
        fig,ax = plt.subplots(1)
        
        for i in range(len(self)):
            
            img = self.getImg(i)
            dat = img.getData()
            
            ax.clear()
            ax.imshow(dat, cmap='Greys', vmin = np.median(dat[dat>0])*0.5, vmax = np.median(dat[dat>0]) / 0.5)
            
            nexRefStar = Utils.centred(self.refStars, dat, r)
            dr = self.driftByCenter(nexRefStar)
            self.refStars = nexRefStar
            self.objectOfInterst = self.objectOfInterst - dr
           
            for j in self.refStars:
                c = Circle(j, radius = r, fill=False)
                ax.add_patch(c)
                c = Circle(j, radius = ri, fill=False)
                ax.add_patch(c)
                c = Circle(j, radius = re, fill=False)
                ax.add_patch(c)
                
            for j in self.objectOfInterst:
                c = Circle(j, radius = r, fill=False)
                ax.add_patch(c)
                c = Circle(j, radius = ri, fill=False)
                ax.add_patch(c)
                c = Circle(j, radius = re, fill=False)
                ax.add_patch(c)
                
            plt.pause(0.01)
            
            
            stars = np.concatenate((self.refStars, self.objectOfInterst))
            self.apperturs.append(Appertur(stars, r = r, ri = ri, re = re))
            self.results.append(self.apperturs[-1].Photom(self.getImg(i), self.key))
            
            print("image: ", i, '\n', self.apperturs[-1].Photom(img, self.key))
    
    def driftByCenter(self, newPos):
        newPos = np.array(newPos)
        return np.mean(np.array(self.refStars) - newPos, axis = 0)
        
    def selectAp(self, r, s):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        isClose = [False]
        img = self.getData()
        
        ax.imshow(img, cmap='Greys', vmin = np.nanmedian(img)*0.5, vmax = np.nanmedian(img)/0.5)
            
        plt.connect('button_press_event', lambda event: Utils.getPosFromImage(event, s, isClose))
        plt.show(block=False)
        
        while not isClose[0]:
            plt.pause(0.01)
            
        
    def phot(self):
        stars = []
        for res in self.results:
            star = []
            for i in range(len(res)):
                star.append(res[i][7])
               
            stars.append(star)
        return np.asarray(stars)
    

    def extractTime(self):
        
        # x = np.zeros((len(self)))
        # for i in range(len(self)):
        #     x[i] = self.getImg(i).getTime(self.key)
        # return x
        
        x = []
        for i in range(len(self)):
            x.append(self.getImg(i).getTime(self.key).to_value('jd'))
        return np.asarray(x)
    
    # def timeFormat(self, tArr, forma):
    #     newArr = []
    #     for i in tArr.to_value(forma):
    #         if forma == 'hms':
    #             newArr = tArr.to_value('isot').split('T')[-1]
    #         else:
    #             newArr = tArr.to_value(forma)
    #     return newArr
    
    def timeFormat(self, tArr, forma):
        if forma == 'hms':
            newArr = tArr.to_value('isot')
            for i in range(newArr.shape[0]):
                newArr[i] = newArr[i].split('T')[-1]
        else:
            newArr = tArr.to_value(forma)
        return newArr

    def plot(self, yRange = None, binning = 1, selection = None, inMag = False, forma = 'jd', xtick = None):
        plt.figure()
        if inMag:
            stars = -2.5*np.log10(Utils.binn(binning, self.phot()))
        else:
            stars = Utils.binn(binning, self.phot())
        print(stars.shape)
        
        x = Utils.binn(binning, self.extractTime())
        x = Time(x, format = 'jd', precision = len(str(x[0]).split('.')[-1]))
        x = self.timeFormat(x, forma)
        
        for i in range(stars.shape[1]):
            plt.scatter(x, stars[:, i])
        
        if inMag:
            plt.gca().invert_yaxis()
   
        if xtick != None:
           plt.xticks(np.linspace(plt.xlim()[0], plt.xlim()[-1], xtick))
           
    
    def toAOTACsv(self, pName, forma = 'jd'):
        
        if len(self.results) == 0:
            print('empty result list')
            return 
        
        x = Utils.binn(1, self.extractTime())
        x = Time(x, format = 'jd', precision = len(str(x[0]).split('.')[-1]))
        x = self.timeFormat(x, forma)
        
        header = ["FrameNo", "Time (UT)"]
        
        for i in range(len(self.results[0])):
            header.append("Signal ("+ str(i+1) + ")")
            header.append("Background ("+ str(i+1) +")")
        
        resultats = []
        for i, res in enumerate(self.results):
            resultat = [i,x[i]]
            
            for re in res:
                resultat.append(re[3])
                resultat.append(re[-2])
            
            resultats.append(resultat)
        
        df = pd.DataFrame(resultats, columns= header)
        df.to_csv(pName, index=False)