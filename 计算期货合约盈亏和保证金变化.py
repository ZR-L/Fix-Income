# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:19:26 2020

@author: 18931
"""
import pandas as pd
#计算期货合约累计盈亏和当日盈亏
M0 = 4500000      #初始保证金
F0 = 30000000     #股指期货合约的出售价格
P0 = 3000         #初始股指期货的交易价格

IF1903_Data = pd.read_excel('F:\数据\第九章/沪深300指数期货合约IF1903（2019年1月至2月）.xlsx',sheet_name="Sheet1",header=0,index_col=0)
IF1903_Return_Total = -F0*(IF1903_Data/P0-1)
IF1903_Return_Total = IF1903_Return_Total.rename(columns={'IF1903结算价':'IF1903累计盈亏'})
IF1903_Return_Daily = IF1903_Return_Total - IF1903_Return_Total.shift(1)
IF1903_Return_Daily.iloc[0] = IF1903_Return_Total.iloc[0]
IF1903_Return_Daily = IF1903_Return_Daily.rename(columns={'IF1903累计盈亏':'IF1903每日盈亏'})
IF1903_Despolt_Daily = IF1903_Return_Total+M0
IF1903_Despolt_Daily = IF1903_Despolt_Daily.rename(columns={'IF1903累计盈亏':'保证金余额'})
Future_Data = pd.concat([IF1903_Return_Daily,IF1903_Return_Total,IF1903_Despolt_Daily],axis=1)

