#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:54:36 2019
-------------------------------------
ETH-Zurich
Geothermal Energy and Gefluids Group
Plasma pulse drillig doctoral projects
Professor Martin Saar
Dr Benjamin Adams & Dr Daniel Vogler
Doctoral candidate: Mohamed Ezzat
Email: m.Ezzat@erdw.ethz.ch
------------------------------------
This script to calculate the voltage across micro-gap by knowing:
1- Electrodes gap distancese
2- Pulse peak voltage (should be the same like your simulation cases in Zapdos)
Required files:
----------------
- No data is required
Output files:
----------------
- capacitance_model   => /data_processing/voltages/c_voltage.csv
- linear_model        => /data_processing/voltages/l_voltage.csv
- resistance_model    => /data_processing/voltages/r_voltage.csv
"""
#------------------------------------
#Required libraries
#------------------------------------
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os
from pandas import DataFrame
import pandas as pd


#%%
#Paschen's law

A     = 112.5  * 1.0e-1  #1/(MPa.um)


gamma = np.log(1.0+(1.0/0.01))
Apn   = A/gamma
print(Apn)

#B     = 2737.5 * 1.0e-4  #kV/(MPa.um)
Bn     = 2737.56 * 1e-4  #kV/(MPa.um)


fs=12


dcrack10  = [ 100, 150., 200., 250.]
dcrack100 = [ 1000, 1500., 2000., 2500. ]

Pr     = 101325.0 * 1.0e-6

d      = np.arange(5, 1000.0, 0.1)

V_bd_n = Bn*Pr*d/np.log(Apn*Pr*d)


#capacitance:
voltage_file= os.path.expanduser("./voltages/c_voltage.csv")
data =pd.read_csv(voltage_file, delimiter=",")
heads=list(data.columns)

vv=data[heads[3]]
pd=data[heads[5]]

print(vv)
print(pd)

fs  = 26 #font_size for the plot
ms  = 16 #marker_size
lws = 4

data     = [[]]
heads    = []
for j in np.arange(12):
    for i, PD in enumerate(Pr*d):
        if round(PD,2) == pd[j]:
            if j<3:
                heads.append("V=200_%s"%(int(pd[j])*10))
            if 3 <= j< 6:
                heads.append("V=300_%s"%(int(pd[j])*10))
            if 6 <= j< 9:
                heads.append("V=400_%s"%(int(pd[j])*10))
            if 9 <= j< 12:
                heads.append("V=500_%s"%(int(pd[j])*10))
            print(j, round(V_bd_n[i]*1.0e3),vv[j])
            data[0].append(round(V_bd_n[i]*1.0e3/vv[j],2))

PlasmaFormation = os.path.expanduser("./voltages/PlasmaFormation.csv")
df = DataFrame(data, columns = heads)
df.to_csv(PlasmaFormation, encoding='utf-8', index=False)


# plt.figure(figsize=(10,7.5))
#
# plt.text(1, 150/1000, "Ionized gas", family="Comic Sans MS", size=fs+6)
# plt.text(1, 10000/1000, "Plasma",  family="Comic Sans MS", size=fs+6)
#
# plt.xscale("log")
# plt.yscale("log")
# plt.ylabel("$V_{P,Min}$ [kV]", fontsize=fs)
# plt.xlabel("$P_{P,i}\cdot d_P$ [$\mathrm{MPa\cdot \mu m}$]", fontsize=fs)
#
# plt.plot(pd[9:12], vv[9:12]/1000, ":<",  markersize=ms, lw=lws,  label="$V_{T,Max}=$ 500 kV")
# plt.plot(pd[6:9],  vv[6:9]/1000,  "-^",  markersize=ms, lw=lws,  label="$V_{T,Max}=$ 400 kV")
# plt.plot(pd[3:6],  vv[3:6]/1000,  "--s", markersize=ms, lw=lws,  label="$V_{T,Max}=$ 300 kV")
# plt.plot(pd[:3] ,  vv[:3]/1000,   "-.*", markersize=ms, lw= lws, label="$V_{T,Max}=$ 200 kV")
# plt.plot(Pr*d, V_bd_n*1.0e3/1000, lw=6, color="black", label="Paschen curve")
#
#
#
#
# miny = 70/1000
# maxy = 70000/1000
# plt.xlim(.5,100)
# plt.ylim(70/1000,70000/1000)
# plt.rcParams['xtick.labelsize']=fs
# plt.rcParams['ytick.labelsize']=fs
# plt.rcParams["mathtext.fontset"] = "cm"
# plt.rcParams["text.usetex"] =True
# plt.fill_between(Pr*d,V_bd_n*1.0e3/1000,maxy,color="LightCyan")
# plt.fill_between(Pr*d,V_bd_n*1.0e3/1000,miny,color="LightGray")
#
# plt.legend(loc=1, numpoints = 1, prop={"size":fs-6})
#
# plt.show()
