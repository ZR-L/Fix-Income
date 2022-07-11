# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:27:41 2021

@author: 18931
"""

import numpy as np
import scipy.stats as st
import math

def VaR(u,vol,p,day):
    return u+vol*st.norm.ppf(p)*np.sqrt(day)

def ES(u,vol,p,day):
    return u+np.sqrt(day)*vol*np.exp(-st.norm.ppf(p)**2/2)/(np.sqrt(2*math.pi)*(1-p))
'''
VaR(预期收益，波动（资产*sigma），置信区间百分比，天数)
ES(预期收益，波动（资产*sigma），置信区间百分比，天数)
注意预期收益是正的话表示亏损
'''
u = -0.5
sigma = 3
q = 0.995
t = 1
a = VaR(u,sigma,q,t)
b = ES(u,sigma,q,t)
print('VaR: ',a)
print('ES: ',b)

def norm(x):
    return st.norm.ppf(x)
c = norm(q)
print('z值为：',c)

