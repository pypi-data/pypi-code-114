# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 17:16:31 2022

@author: nicol
"""

def NumPrimo(n):
    if n==1:
        return True
    elif n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True


def NumPares(n):
    pares=[]
    for i in range(1,n+1):
        if (i%2==0):
            pares.append(i)
    return pares