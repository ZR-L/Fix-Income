# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:21:59 2020

@author: 18931
"""

#方法：设定1000组随机数权重，分别计算收益率和波动率，寻找有效前沿
import pandas as pd
import numpy as np

Excel_name = 'F:\数据\第八章/构建投资组合的五只股票数据.xlsx'
data = pd.read_excel(Excel_name,sheet_name="Sheet1",header=0,index_col=0)
data.head()
R = np.log(data/data.shift(1))  #shift(1)表示前一行这个位置的数据
R = R.dropna()
R.describe()
R_mean = R.mean()*252    #年化平均值
R_cov = R.cov()*252      #年化协方差矩阵
R_corr = R.corr() 

Rp_list = []
Vp_list = []
for i in np.arange(1000):
    x = np.random.random(5)
    weights = x/np.sum(x)
    Rp_list.append(np.sum(weights*R_mean))
    Vp_list.append(np.sqrt(np.dot(weights,np.dot(R_cov,weights.T))))
   
import scipy.optimize as sco
def f(w):     #定义一个需要求解最优化的函数 
    w = np.array(w)
    Rp_opt = np.sum(R_mean*w)
    Vp_opt = np.sqrt(np.dot(w,np.dot(R_cov,w.T)))
    return np.array([Rp_opt,Vp_opt])
def Vmin_f(w):    #定义一个得到最小波动率V的权重函数 
    return f(w)[1]    #输出前面定义函数f(w)的第二个元素
cons = {'type':'eq','fun':lambda x:np.sum(x)-1},{'type':'eq','fun':lambda x:f(x)[0]-0.1}
#以字典的形式输入约束条件，翻译过来是：权重之和等于1，收益率等于0.1
bnds = tuple((0,1) for x in range(len(R_mean))) #输入边界条件
L = len(R_mean)*[1/len(R_mean)]  #生成一个于权重相等个数元素的数组
result = sco.minimize(Vmin_f,L,method='SLSQP',bounds=bnds,constraints=cons)

#找全局的最小值
cons2 = {'type':'eq','fun':lambda x:np.sum(x)-1}
result_vmin = sco.minimize(Vmin_f,L,method='SLSQP',bounds=bnds,constraints=cons2)














