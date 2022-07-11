# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:13:14 2020

@author: 18931
"""
import numpy as np
def CAPM(beta,Rm,Rf):
    return Rf+beta*(Rm-Rf)
import pandas as pd
data_index = pd.read_excel('F:\数据\第八章/沪深300指数（2016-2018年）.xlsx',sheet_name="Sheet1",header=0,index_col=0)
R_index = np.log(data_index/data_index.shift(1))
R_index = R_index.dropna()
R_index.describe()
R_data = pd.read_excel('F:\数据\第八章/1.xlsx',sheet_name="Sheet1",header=0,index_col=0)
import statsmodels.api as sm
R_index_addcons = sm.add_constant(R_index) #加一列常数项，做线性回归的时候用
R_model = sm.OLS(endog=R_data.iloc[:,0],exog=R_data.iloc[:,1])
R_result = R_model.fit()
a=R_result.params
