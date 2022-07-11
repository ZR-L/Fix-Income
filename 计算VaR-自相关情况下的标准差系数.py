# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:45:13 2021

@author: 18931
"""
import numpy as np
def f1(T,p):
    List1=[T]
    n=1
    while T>0:
        List1.append(2*(T-n)*p**n)
        T=T-1
        print(T)
        n=n+1
    while T<1:
        return np.sqrt(np.sum(List1))
    return np.sqrt(np.sum(List1))
A = f1(5,0.05)
print(A)
