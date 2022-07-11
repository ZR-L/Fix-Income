# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:10:17 2020

@author: 18931
"""

import numpy as np
import scipy.optimize as so
def f(R):
    return 100*(1+0.0277)-100.09*np.exp(R)
a = so.fsolve(f,0.01)

year = [0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0]
Y = [0.023268,0.023538,0.025155,0.026424,0.026184,0.025411,0.025617,0.028313]

def Value(M,r,m):
    Cash_flow = []
    for i,y in zip(year,Y):
        Cash_flow.append(np.sum(np.exp(-y*i)*M*r/m))
    return np.sum(Cash_flow)+np.exp(-0.028313*2)*M
b = Value(M=100,r=0.06,m=4)
print(b)
