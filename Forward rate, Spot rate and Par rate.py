# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:22:32 2021

@author: 18931
"""

import numpy as np
import sympy
from sympy import solveset, S  


def product(A):
    '''
    Argument:
        A is list
    this function can calculate cumlative product of list A's item plus 1
    '''
    B = []
    a=1
    for i in A:
        a = a*(i+1)
        B.append(a)
    return(B)

    
def fr_sr(fr,sr,cal):
    '''
    Argument:
        fr: list for forward rate
        sr: list for sopt rate
        cal: str for choose which rate we need to calculate
    for this function, you need also type the term you want to calculate as an empty list
    '''
    if cal == "sr":
        l = len(fr)
        L = np.arange(1,l+1)
        fr1 = product(fr)            # calculate cumlative product of fr's term
        for i,k in zip(fr1,L):
            sr.append(pow(i,1/k)-1)  # calculate spot rate
        return(sr)
        print('spot rates are:',sr)

    if cal == "fr":
        sr1=[1]
        l = len(sr)
        L = np.arange(1,l+1)       
        for i,k in zip(sr,L):
            sr1.append((1+i)**k)     # calculate the divisior we need below
        sr2 = sr1[0:l]               # this list contains the numerators
        sr3 = sr1[1:l+1]             # this list contains the denominators
        for i,k in zip(sr2,sr3):
            fr.append(k/i-1)
        return(fr)
        print('forward rates are:',fr)



def sr_pr(sr,pr,t,pv,par,cal):
    '''
    Argument:
        sr: list for spot rates
        pr: lsit for different bonds
        t:  value for maturity time of a certain bond
        pv: present value (sell price) for each bond
        par: par value for each bond
        cal: str for choose which rate we need to calculate
    '''
    T = np.arange(1,t+1)
    if cal == "pr":
        pvlist = []
        x = sympy.Symbol('x')     # set a variable
        for i,k in zip(sr,T):
            pvlist.append(x*par/(1+i)**k)
        a = sr[-1]
        pvsum = np.sum(pvlist)+par/(1+a)**t   #using formula calculate present value
        fx = pvsum - pv
        # let fx=0, which means present value = par value, we can solve x
        result = sympy.solve(fx,x) 
        return(result)
    
    if cal == "sr":
        sr = [pr[0]]
        for i in T[1:len(T)]:  # for a certain year, we only have one par rate
            pr1 = pr[i-1]
            pvlist = []
            for j,q in zip(T[0:i-1],sr):   #under this par rate, we do the calculation
                # calculate the present value except the last period
                pvlist.append(par*pr1/(1+q)**j)  
                x = sympy.Symbol('x')
                # calculate the present value of the last period by using variable 'x'
                sumpy = np.sum(pvlist) + par*(1+pr1)/(1+x)**i
                fx = sumpy - pv
                result = solveset(fx,x,domain=S.Reals) # solve the equation under real numbers
                result1 = [n for n in result if 0<n<1] # choose the result with finance means
                result2 = result1[0]                   # change list to a number
            sr.append(result2)                         # add the result to the sr list
        return(sr)




'''
By using these two function ('fr_sr' and 'sr_pr'), we can convert forward rate,
spot rate and par rate.

for example:  
convert forward rate to spot rate:
    1.set two list fr = [each forward rate] and sr = []
    2.using fr_sr function: fr_sr(fr,sr,"sr")

convert spot rate to forward rate:
    1.set two list sr = [each spot rate] and fr = []
    2.using fr_sr function: fr_sr(fr,sr,"fr")
    
convert spot rate to par rate:
    1.set two list sr = [each spot rate] and pr = []
    2.find time period you need, the par value of this bond and the sell price of each bond
    3.using fr_sr function: sr_pr(fr,sr,t,pv,par"fr")

convert par rate to spot rate:
    1.set two list pr = [each par rate] and sr = []
    2.find time period you need, the par value of this bond and the sell price of each bond
    3.using fr_sr function: sr_pr(fr,sr,t,pv,par"fr")

By using these two functions, if we knwo two of these three rates, we can
calculate another one.
'''
        
























