# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:39:45 2021

@author: 18931
"""
import numpy as np
def sigma(w1,w2,v1,v2,p):
    print('相关系数为:')
    return np.sqrt(w1**2*v1**2+w2**2*v2**2+2*w1*w2*v1*v2*p)

w1 = -3
w2 = 2
v1 = 0.007
v2 = 0.005
p = 0.9
a = sigma(-3,2,0.007,0.005,0.9)
print(a)
