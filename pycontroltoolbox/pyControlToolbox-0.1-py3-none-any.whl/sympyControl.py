import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

s = sp.symbols('s', real=False)
t,w = sp.symbols('t w', real=True)
j = sp.I

def tf(numCoef=0,denCoef=1):    #order is: coef of highest power of s->lowest
    num = 0
    den = 0
    numList = numCoef[::-1]     #small arrays, no need for numpy quickness
    denList = denCoef[::-1]
    if(numCoef!=0 and denCoef!=0): 
        for i,coef in enumerate(numList):   #for this to work we need reversed order
            num += coef*(s**i)
            for i,coef in enumerate(denList):
                den += coef*(s**i)
    return num/den
     

def laplace(func):
    sfunc = sp.integrate(func*sp.exp(-s*t),(t,0,sp.oo))
    return sfunc

def invlaplace(sys):
    tfunc = sp.inverse_laplace_transform(sys,s,t)
    return tfunc

def step(sys,time=1):
    stepS = 1/s
    dt = time/1000
    timeNow = 0
    responseVec = np.array([])
    timeVec = np.array([])
    Sresponse = stepS*sys
    response = invlaplace(Sresponse)
    while(timeNow<time):
        temp = response.evalf(subs={t:timeNow})
        # print(temp)
        # print(timeNow)
        if(timeNow>0):
            responseVec = np.append(responseVec,temp)
            timeVec = np.append(timeVec,timeNow)
        timeNow+=dt
    fig = plt.subplot()
    fig.plot(timeVec, responseVec)
    fig.set_xlabel('Time [s]')
    fig.set_ylabel('Amplitude')
    fig.set_title("Step response")
    return fig
        

        
