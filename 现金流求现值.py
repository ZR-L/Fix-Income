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
T：到期时间
n：每年计息次数
"""


Cash_flow = []
def Value(P,n,r,R,T):
    List1=range(1,T*n+1)
    print(List1)
    for t in List1:
        Cash_flow.append(P*R/n/pow(1+r,t/n))
    return sum(Cash_flow,P/pow((1+r),T))
V = Value(100,2,0.03,0.02,5)
print(V)

