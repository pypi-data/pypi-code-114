#!/usr/bin/env python
# coding: utf-8

# In[4]:


import scipy.special as sc
import numpy as np
from mpmath import *
mp.dps = 10; mp.prec = 60; mp.pretty = True
def Lsp(r,p,Q,T,S,tq,ts):
    phi = sqrt(p*T*(1+p*tq)/(S+p*S*ts))
    q = -Q/(2*np.pi*T*p)
    sp = q*besselk(0, r*phi)
    return sp

def Lst(r,t,Q,T,S,tq,ts):
    ap = lambda p: Lsp(r,p,Q,T,S,tq,ts)
    return invertlaplace(ap,t,method='deHoog')

def Lagfunc(r,tt,Q,T,S,tq,ts):
   nrow = len(tt)
   n= nrow
   drawdown=np.zeros((n),float)
   for i in range (0,n):
      LagW_val=Lst(r,tt[i],Q,T,S,tq,ts)
      drawdown[i] = LagW_val
   #End loop i
   return (drawdown)

