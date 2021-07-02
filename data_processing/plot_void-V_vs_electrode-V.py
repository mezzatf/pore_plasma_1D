
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
This script to plot the void voltage vs the total electrode voltage
Required data files:
----------------------
- capacitance_model   => /data_processing/voltages/c_voltage.csv
- linear_model        => /data_processing/voltages/l_voltage.csv
- resistance_model    => /data_processing/voltages/r_voltage.csv
if these files are not in the same dir, you can reproduce them
by running this python_script: ./void_voltage_calculator.py
Output files:
- foe each block below, a fig will be generated (V_void vs V_total)
How to run:
run by block not the whole file at once
"""

#------------------------------------
#Required libraries
#------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k, R
import os
import pandas as pd

#%%
#First block
######### capacitance_model ###################
#plot the void voltage across the total electrode voltage (c_model)
voltage_file= os.path.expanduser("./voltages/c_voltage.csv")
data =pd.read_csv(voltage_file, delimiter=",")
heads=list(data.columns)

vv=data[heads[3]]
vt=data[heads[0]]
de=data[heads[2]]


l10=[0,3,6,9]
l50= [x+1 for x in l10]
l100= [x+1 for x in l50]

fs  = 26 #font_size for the plot
ms  = 16 #marker_size
lws = 6
fig=plt.figure(figsize=(8,6))
plt.ylabel("$V_{P,Max}\; \mathrm{[kV]}$", fontsize=fs)
plt.xlabel("$V_{T,Max}\; \mathrm{[kV]}$", fontsize=fs)
plt.plot(vt[l10], vv[l10]/1000.0, "-.D", markersize=ms, lw=lws, color="orange", label="$d=10 \mathrm{\mu m}$")
plt.plot(vt[l50], vv[l50]/1000.0, "--s", markersize=ms, lw=lws, color="green", label="$d=50 \mathrm{\mu m}$")
plt.plot(vt[l100], vv[l100]/1000.0,"-^", markersize=ms, lw=lws, color="grey", label="$d=100 \mathrm{\mu m}$")
plt.rcParams['xtick.labelsize']=fs
plt.rcParams['ytick.labelsize']=fs
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["text.usetex"] =True
plt.grid(color='grey', which="both",ls="--")
plt.rc('font', size=fs)
fig.subplots_adjust(bottom=0.20)
plt.legend(loc=2, fontsize="large", numpoints = 1, prop={"size":fs-6})
plt.xlim(100,600)
plt.ylim(0,15)

plt.show()


# #%%
# #second block
# ######### linear_model ###################
# #plot the void voltage across the total electrode voltage (l_model)
# voltage_file= os.path.expanduser("./voltages/l_voltage.csv")
# data =pd.read_csv(voltage_file, delimiter=",")
# heads=list(data.columns)
#
# vv=data[heads[3]]
# vt=data[heads[0]]
# de=data[heads[2]]
#
#
# l10=[0,3,6]
# l50= [x+1 for x in l10]
# l100= [x+1 for x in l50]
#
# plt.figure(2)
# fs = 18
# lws =4
# ms=16
# plt.ylabel("$\mathrm{Linear,\;V_{v}}$ [kV]", fontsize=fs)
# plt.xlabel("$\mathrm{V_{T}}$ [kV]", fontsize=fs)
# plt.plot(vt[l10], vv[l10]/1000.0, "-.*", markersize=ms, lw=lws, label="d=10 $\mu m$")
# plt.plot(vt[l50], vv[l50]/1000.0, "--s", markersize=ms, lw=lws,label="d=50 $\mu m$")
# plt.plot(vt[l100], vv[l100]/1000.0,"-^", markersize=ms, lw=lws, label="d=100 $\mu m$")
# plt.rcParams['xtick.labelsize']=fs
# plt.rcParams['ytick.labelsize']=fs
# plt.legend(loc=0, fontsize="xx-large")
# plt.grid(color='grey', which="both",ls="--")
#
# plt.show()
#
#
# #%%
# #third block
# ######### resistance_model ###################
# #plot the void voltage across the total electrode voltage (r_model)
# voltage_file= os.path.expanduser("./voltages/r_voltage.csv")
# data =pd.read_csv(voltage_file, delimiter=",")
# heads=list(data.columns)
#
# vv=data[heads[3]]
# vt=data[heads[0]]
# de=data[heads[2]]
#
#
#
# l10=[0,3,6]
# l50= [x+1 for x in l10]
# l100= [x+1 for x in l50]
#
# plt.figure(3)
# fs = 18
# lws =4
# ms=16
# plt.ylabel("$\mathrm{Resistance, \;V_{v}}$ [kV]", fontsize=fs)
# plt.xlabel("$\mathrm{V_{T}}$ [kV]", fontsize=fs)
# plt.plot(vt[l10], vv[l10]/1000.0, "-.*", markersize=ms, lw=lws, label="d=10 $\mu m$")
# plt.plot(vt[l50], vv[l50]/1000.0, "--s", markersize=ms, lw=lws,label="d=50 $\mu m$")
# plt.plot(vt[l100], vv[l100]/1000.0,"-^", markersize=ms, lw=lws, label="d=100 $\mu m$")
# plt.rcParams['xtick.labelsize']=fs
# plt.rcParams['ytick.labelsize']=fs
# plt.legend(loc=0, fontsize="xx-large")
# plt.grid(color='grey', which="both",ls="--")

plt.show()
