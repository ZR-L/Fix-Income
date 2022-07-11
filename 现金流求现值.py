# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 20:05:45 2020

@author: 18931
"""


#计算债券现值程序
"""
P:票面价值
R：利息率
r：贴现率
n：每年计息次数
T：到期时间
"""

#复利
Cash_flow = []
def Value(P,R,r,n,T):
    List1=range(1,T*n+1)
    for t in List1:
        Cash_flow.append(P*R/n/pow(1+r/n,t))
    return sum(Cash_flow,P/pow((1+r/n),n*T))
V = Value(100,0.02,0.03,2,5)
print(V)

#连续复利
import numpy as np
Cash_flow2 = []
def Value2(P,R,r,n,T):
    List2=range(1,T*n+1)
    for i in List2:
        Cash_flow2.append(P*R/n*np.exp(-r*i/n))
    return sum(Cash_flow2,P*np.exp(-T*r))
V2 = Value2(100,0.02,0.03,2,5)
print(V2)