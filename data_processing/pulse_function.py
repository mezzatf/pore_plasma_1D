#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:15:00 2019

@author: M.Ezzat
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k, R
import os
import math

PowerFile = os.path.expanduser('./Lisitsyn_1998_pulse_profile.csv')
data      = pd.read_csv(PowerFile, delimiter=",")
TExp      = data['time']
VExp      = data['volt']

VMax  =   max(VExp)
VNorm =   VExp


Vo  = 503
Lam = 700
S   = 30

TA = np.arange(-1,2.4*1e-6,0.01*1e-6)
VA = []

for t in TA:
    t = t-60
    V   = Vo/2.0 * np.exp( (S/(2*Lam))**2 - t/Lam ) * math.erfc(S/(2.0*Lam) - (t/S))
    VA.append(V)

print(max(np.array(VA)))
print(VMax)
plt.plot([100,100],[0,Vo])
plt.plot([-10,2000],[Vo,Vo])

plt.plot(TA, VA)
plt.plot(TExp*1e3, VExp)
plt.ylim(0,Vo+10)
plt.show()
