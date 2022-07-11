# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:29:02 2021

@author: 18931
"""

import numpy as np
import scipy.stats as st
u1 = 0.082
sigma = 0.3
T = 2
def prob(S,V):
    d2 = (np.log(S/V)+(u1-0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    print('d2=',d2)
    if S>V:
        print('the prob',S,'>',V,'is')
        return st.norm.cdf(d2)
    if S<V:
        print('the prob',S,'<',V,'is')
        return st.norm.cdf(-d2)
    
a = prob(100,110)
print(a)


u2 = 0.08
sigma2 = 0.2
t = 0.5
def V(S,q,d):
    if d <= 1:
        print('最大可能值为')
        return S*np.exp((u2-sigma2**2/2)*t+st.norm.ppf(q)*sigma2*np.sqrt(t))
    if d>1:
        print('最小可能值为')
        return S*np.exp((u2-sigma2**2/2)*t-st.norm.ppf(q)*sigma2*np.sqrt(t))
b = V(80,0.99,2)

print(b)
    

