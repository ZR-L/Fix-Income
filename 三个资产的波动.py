# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:05:42 2021

@author: 18931
"""
import numpy as np

sa = 0.2
sb = 0.3
sc = 0.5

pab = 0.3
pac = 0.5
pbc = -0.1

w1 = 0.4
w2 = 0.3
w3 = 1- w1 - w2

saa = sa**2
sbb = sb**2
scc = sc**2
sab = pab * sa * sb
sac = pac * sa * sc
sbc = pbc * sb * sc

P1 = np.array([saa,sab,sac])
P2 = np.array([sab,sbb,sab])
P3 = np.array([sac,sbc,scc])
print(P1,P2,P3)

W = [w1,w2,w3]
print('w',W)

P = [pab,pac,pbc]
print('P',P)

cal1 = w1*saa+w2*sab+w3*sac
cal2 = w1*sab+w2*sbb+w3*sbc
cal3 = w1*sac+w2*sbc+w3*scc

print('cal',cal1,cal2,cal3)

Pvar = cal1*w1+cal2*w2+cal3*w3
print('Pvar',Pvar)