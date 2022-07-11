# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:52:51 2020

@author: 18931
"""

#计算期货套期保值比率
import pandas as pd
data2 = pd.read_excel('F:\数据\第九章\上证180ETF与期货合约的数据.xlsx',sheet_name="Sheet1",header=0,index_col=0)
#分别计算收益率
SH180ETF_return = data2.iloc[:,0]/data2.iloc[:,0].shift(1)-1
SH180ETF_return = SH180ETF_return.dropna()
IF1812_return = data2.iloc[:,1]/data2.iloc[:,1].shift(1)-1
IF1812_return = IF1812_return.dropna()
IC1812_return = data2.iloc[:,2]/data2.iloc[:,2].shift(1)-1
IC1812_return = IC1812_return.dropna()
IH1812_return = data2.iloc[:,3]/data2.iloc[:,3]-1
IH1812_return = IH1812_return.dropna()

import statsmodels.api as sm
IF1812_return_addcons = sm.add_constant(IF1812_return) #分别添加常数项
IC1812_return_addcons = sm.add_constant(IC1812_return)
IH1812_return_addcons = sm.add_constant(IH1812_return)
#建立模型，选择拟合程度最高的进行对冲
model_SH180_IF1812 = sm.OLS(SH180ETF_return,IF1812_return_addcons).fit()  
model_SH180_IC1812 = sm.OLS(SH180ETF_return,IC1812_return_addcons).fit()
model_SH180_IH1812 = sm.OLS(SH180ETF_return,IH1812_return_addcons).fit()
