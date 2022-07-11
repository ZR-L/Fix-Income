# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:55:21 2020

@author: 18931
"""
#计算夏普比率
import pandas as pd
import numpy as np
L = 'F:\数据\第八章/四只开放式股票型基金的净值（2016-2018年）.xlsx'


Fund = pd.read_excel(L,sheet_name="Sheet1",header=0,index_col=0)
R_fund = np.log(Fund/Fund.shift(1))
R_fund = R_fund.dropna()
R_mean = R_fund.mean()*252
Sigma = R_fund.std()*np.sqrt(252)

def SR(Rf,Rm,Vp):
    return (Rm-Rf)/Vp

SR_3years = SR(Rf=0.015,Rm=R_mean,Vp=Sigma)
print(SR_3years)