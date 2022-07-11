# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:34:03 2020

@author: 18931
"""
import pandas as pd
import numpy as np
'''input'''
Excel_name = 'F:\数据\第八章/构建投资组合的五只股票数据.xlsx'
weights = [0.2,0.2,0.2,0.2,0.2]

weights = np.array(weights)
data = pd.read_excel(Excel_name,sheet_name="Sheet1",header=0,index_col=0)
data.head()
R = np.log(data/data.shift(1))  #shift(1)表示前一行这个位置的数据
R = R.dropna()
R.describe()
R_mean = R.mean()*252    #年化平均值
R_cov = R.cov()*252      #年化协方差矩阵
R_corr = R.corr()        #相关系数矩阵
R_port = np.sum(weights*R_mean)
vol_port = np.sqrt(np.dot(weights,np.dot(R_cov,weights.T)))  #np.dot()用于矩阵的乘法

'''output'''
print(R_port)
print(vol_port)


