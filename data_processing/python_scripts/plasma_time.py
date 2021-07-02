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






tt = np.arange(0.0, 1.2,1e-4)*1e-6
T  = np.array([3e6, 9e6, 27e6])

PlasmaVoltFile = os.path.expanduser('./voltages/PlasmaFormation.csv')
PlasmaVolt     = pd.read_csv(PlasmaVoltFile, delimiter=",")
PlasmaVoltKeys = PlasmaVolt.keys()



markers = [":", "--", "-"]
colors  = ["green", "blue", "red"]
Labels  = ["$\\tau_R=\;300\; \mathrm{ns}$", "$\\tau_R=\;100\; \mathrm{ns}$", "$\\tau_R=\;30\; \mathrm{ns}$"]

fs  = 26 #font_size for the plot
ms  = 16 #marker_size
lws = 6
plt.figure(figsize=(12,7.5))

#plt.axvspan(0, 500, ymax=0.91 ,alpha=0.5, color='Grey', label="$\\tau_D =\; 500\; \mathrm{ns}$")
plt.plot(TExp, VNorm, markersize=ms, lw= lws, color="black", label="$\mathrm{Experiment}$")
Count = 0
TimeData = []
for i in np.arange(2,-1,-1):
    TimeDataStep = []
    for ii in np.arange(len(PlasmaVoltKeys)):
        VV = np.tanh(tt*T[i])
        for j, V in enumerate(VV):
            if  round(V,2) == PlasmaVolt[PlasmaVoltKeys[ii]][0]:
                Count += 1
                print(i, Count, j)
                TimeDataStep.append(round(tt[j]*1e9,2))
                print(round(V,2), PlasmaVolt[PlasmaVoltKeys[ii]][0])
                break
    TimeData.append(TimeDataStep)

PlasmaTimeFile = os.path.expanduser("./voltages/PlasmaTimeFile.csv")
PlasmaTime = DataFrame(TimeData, columns = list(PlasmaVoltKeys))
PlasmaTime.to_csv(PlasmaTimeFile, encoding='utf-8', index=False)



#         plt.plot(tt[:] * 1e9 , VV[:], markers[i], markersize=ms, lw= lws, color=colors[i], label=Labels[i])
#
# X = 500
# plt.ylabel("$f\\left(t\\right)$", fontsize=fs)
# plt.xlabel("$t\mathrm{[ns]}$", fontsize=fs)
# plt.xlim(0,2000)
# plt.ylim(0,1.1)
# plt.grid(color='grey', which="both",ls="--")
# plt.rcParams['xtick.labelsize']=fs
# plt.rcParams['ytick.labelsize']=fs
# plt.rcParams["mathtext.fontset"] = "cm"
# plt.rcParams["text.usetex"] =True
# plt.legend(loc=7, numpoints = 1, prop={"size":fs})
# #NP = np.array([0,200,400,500,600,800,1000,1200])
# #plt.xticks(NP, ('0','200','400','$\\tau_D$','600','800','1000','1200'))
# plt.show()
