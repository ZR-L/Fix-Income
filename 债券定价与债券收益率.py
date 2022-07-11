# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 08:46:34 2020

@author: 18931
"""

#利率的复利频次
def f(x):
    return 100*(1+0.02/x)**x
a = f(12)
print(a)
M = [1,2,4,12,52,365]
for i in M:
     print('复利的次数',':',i,f(i))
  
#连续复利的计算
import numpy as np
def Rc(Rm,m):                 #RM为复利m次的复利利率 Rc为等价连续复利利率
    return m*np.log(1+Rm/m)   #输出等价的连续复利利率结果

def Rm(Rc,m):
    return m*(np.exp(Rc/m)-1)   #输出与连续复利Rc等价的m频次的利率Rm

#债券的定价公式
coupon = []
def Bond_price(C,M,T,m,y):
    for i in np.arange(1,T*m+1):
       coupon.append(np.exp(-y*T/m)*M*C/m)
       return np.sum(coupon)+np.exp(-y*T)*M


Bond = Bond_price(C=0.0525,M=100,T=10,m=2,y=0.042)
print(Bond)
    
#计算债券到期收益率
import scipy.optimize as so
def YTM(C,M,T,m,P):
    def f(y):
        coupon2=[]
        for i in np.arange(1,m*T+1):
            coupon2.append(np.exp(-y*i/m)*M*C/m)   #每一期的利率折现
        return np.sum(coupon2)+np.exp(-y*T)*M-P
    return so.fsolve(f,0.1)

Bond_yeild = YTM(C=0.05,M=100,T=5,m=2,P=98)
print(Bond_yeild)
        
        
        
        