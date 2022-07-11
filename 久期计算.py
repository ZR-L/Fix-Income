# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:26:30 2020

@author: 18931
"""

#麦考利久期
import numpy as np

def D(m,y,T,M,r):
    cash = []
    for t in np.arange(1,m*T+1)/m:
        cash.append(np.exp(-y*t)*M*r/m)
        B = np.sum(cash)+M*np.exp(-y*T)
    Duration = []
    for t in np.arange(1,m*T+1)/m:
        Duration.append((np.exp(-y*t)*M*r/m)/B*t)
    return np.sum(Duration)+(np.exp(-y*T)*M)/B*T
a = D(m=2,y=0.038,r=0.0295,M=100,T=4)
print(a)

'''
T：到期期限
m：每年计息次数
M：票面价值
y：到期收益率（贴现率）
r：票面利率
'''