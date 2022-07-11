# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:20:43 2020

@author: 18931
"""
#模拟股价
import numpy as np
import pandas as pd
S = pd.read_excel('F:\数据\第八章/东方航空股票价格（2014-2018）.xlsx',sheet_name="Sheet1",header=0,index_col=0)
R = np.log(S/S.shift(1))
R = R.dropna()
mean = R.mean()*252
vol = R.std()*np.sqrt(252)
print(round(mean,4))
print(round(vol,4))
import numpy.random as npr
date = pd.DatetimeIndex(start='2019-01-02',end='2021-12-31',freq='B')  #生成需要预测的时间的序列
N = len(date)
 #模拟路径数
dt = 1.0/252
I = 500
mean = np.array(mean) #将数据调整为数组
vol = np.array(vol)
S_GBM = np.zeros((N,I))  #生成一个与（N,I)矩阵有相同的元素和排列且全是0的矩阵,用于存放后面产生的数据
S_GBM[0] = 4.73 #设置起始点
for t in range(1,N):
    epsilon = npr.standard_normal(I) #产生随机数，呈正态分布 
    S_GBM[t] = S_GBM[t-1]*np.exp(mean-0.5*vol**2)*dt+vol*epsilon*np.sqrt((dt))
S_GBM = pd.DataFrame(S_GBM,index=date)





