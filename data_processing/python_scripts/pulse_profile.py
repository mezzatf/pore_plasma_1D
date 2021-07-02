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
import pandas as pd
from numpy import trapz


PowerFile = os.path.expanduser('./Lisitsyn_1998_pulse_profile.csv')
data      = pd.read_csv(PowerFile, delimiter=",")
TExp      = data['time']*1e3
VExp      = data['volt']

VMax  =   max(VExp)
VNorm =   VExp/VMax

AreaExp = 0
for ii in np.arange(len(VNorm)-1):
    if TExp[ii] <= 2000:
       AreaExp += (VNorm[ii+1] + VNorm[ii]) * (TExp[ii+1] - TExp[ii])/2.0

print(AreaExp)



# Compute the area using the composite trapezoidal rule.


tt = np.arange(0.0, 1.2,1e-3)*1e-6
T  = np.array([3e6, 9e6, 27e6])



markers = [":", "--", "-"]
colors  = ["green", "blue", "red"]
Labels  = ["$\\tau_R=\;300\; \mathrm{ns}$", "$\\tau_R=\;100\; \mathrm{ns}$", "$\\tau_R=\;30\; \mathrm{ns}$"]

fs  = 26 #font_size for the plot
ms  = 16 #marker_size
lws = 6
plt.figure(figsize=(13,7.5))

EndValues=[]
#plt.axvspan(0, 500, ymax=0.91 ,alpha=0.5, color='Grey', label="$\\tau_D =\; 500\; \mathrm{ns}$")
plt.plot(TExp[::2], VNorm[::2], "-o", markersize=ms,  lw= lws, color="black", label="$\mathrm{Experiment}$")
for i in np.arange(2,-1,-1):
    VV = np.tanh(tt*T[i])
    AreaTh = 0
    for ii in np.arange(len(VV)-1):

        if AreaExp >= AreaTh:
           AreaTh += (VV[ii+1] + VV[ii]) * (1)/2.0
           m = ii


    print(m, AreaTh)
    EndValues.append(tt[m]* 1e9)
    plt.plot(tt[:m+1] * 1e9 , VV[:m+1], markers[i], markersize=ms, lw= lws, color=colors[i], label=Labels[i]+", $\\tau_D=%3.0f\; \mathrm{ns}$"%(tt[m]* 1e9))
    plt.plot([tt[m]* 1e9, tt[m]* 1e9]  , [0,1], markers[i], markersize=ms, lw= lws, color=colors[i])

X = 500
plt.ylabel("$f\\left(t\\right)$", fontsize=fs)
plt.xlabel("$t\mathrm{[ns]}$", fontsize=fs)
plt.xlim(0,2000)
plt.ylim(0,1.1)
plt.grid(color='grey', which="both",ls="--")
plt.rcParams['xtick.labelsize']=fs
plt.rcParams['ytick.labelsize']=fs
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["text.usetex"] =True
plt.legend(loc=7, numpoints = 1, prop={"size":fs})
# plt.xticks([0,250,500,EndValues[0],EndValues[1],EndValues[2],1000,1250,1500,1750,2000], rotation=45)
plt.show()
