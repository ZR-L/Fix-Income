# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:33:24 2021

@author: 18931
"""


#投资组合均值和标准差计算
#R为预期收益，v为标准差
import numpy as np
R1 = 0.08
v1 = 0.14
R2 = 0.12
v2 = 0.20
p = 0.3
ListR = []
ListV = []
    
for w1 in [0,0.2,0.4,0.6,0.8,1]:
    w2 = 1-w1
    ListR.append(R1*w1 + R2*w2)
    ListV.append(np.sqrt(w1**2*v1**2+w2**2*v2**2+2*p*w1*w2*v1*v1))
      
print('收益分别为：',ListR)
print('波动分别为：',ListV)
    
