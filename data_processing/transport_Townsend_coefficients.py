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
Email: m.ezzat@erdw.ethz.ch
------------------------------------
This script to calculate:
1- Plasma pressure at differnet operation voltages
2- Energy desnity profile versus time.

Required files:
----------------
We have 12 case that corresponds this following combination:
case_index is on of the all reuired indices here
261, 262, 263, 264 corresponds 200, 300, 400, 500 kV at micro-gap=10 um
265, 266, 267, 268 corresponds 200, 300, 400, 500 kV at micro-gap=50 um
269, 270, 271, 272 corresponds 200, 300, 400, 500 kV at micro-gap=100 um
Output:
----------------
wop is a parameter, exist after libs.
If wop = 1 => Figure (Pressure versus voltage).
If wop = 2 => Figure (Energy density versus timeself.
If wop = 3 => Figure (Pulse profile voltage versus time).
"""
#------------------------------------
#Required libraries
#------------------------------------
from netCDF4 import Dataset
import sys
import matplotlib.pyplot as plt
import os
from scipy.constants import e, m_e, k, R
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.gridspec as gridspec


# coefficients_file = os.path.expanduser('./td_nitrogen_mean_en.csv')
# data =pd.read_csv(coefficients_file, delimiter=" ")
# heads=list(data.columns)

coefficients_file = open('./td_nitrogen_mean_en.txt', "r")
ReadLine = coefficients_file.readlines()
EField = []
Mobility, Diffusion = [],[]
Ionization, Excitation, IonizationSec  = [],[],[]

for line in ReadLine:
    EField.append (float(line.split('\t')[0]))
    Mobility.append (float(line.split('\t')[1]))
    Diffusion.append (float(line.split('\t')[2]))
    Ionization.append (float(line.split('\t')[3]))
    Excitation.append (float(line.split('\t')[4]))
    IonizationSec.append (float(line.split('\t')[5]))


fs  = 18 #font_size for the plot
ms  = 10 #marker_size
lws = 3
plt.figure(figsize=(11,8))
gs = gridspec.GridSpec(3,4)
gs.update(wspace=0.7, hspace=0.2)
for i in range(5):

    if i==0:
        ax = plt.subplot(gs[0,:2])
        plt.plot(EField, Mobility, "*", markersize=ms, color="orange",  label="BOLSIG+")
        plt.plot(EField, Mobility, "-",  lw=lws, color="grey", label="Splin")
        plt.ylabel("$\\mu_e\; \mathrm{[m^2/s/V]}$", fontsize=fs)
        plt.legend(loc=0, fontsize="xx-large",  numpoints = 1)
        ax.set_xticklabels([])
    if i==1:
        ax = plt.subplot(gs[1,:2])
        plt.plot(EField, Diffusion, "*", markersize=ms, color="orange",  label="BOLSIG+")
        plt.plot(EField, Diffusion, "-",  lw=lws, color="grey", label="Splin")
        plt.ylabel("$D_e\; \mathrm{[m/s^2]}$", fontsize=fs)
        plt.xlabel("$\epsilon \mathrm{[eV]}$", fontsize=fs)
    if i==2:
        ax = plt.subplot(gs[0,2:4])
        plt.plot(EField, Ionization, "*", markersize=ms, color="orange",  label="BOLSIG+")
        plt.plot(EField, Ionization, "-",  lw=lws, color="grey", label="Splin")
        plt.ylabel("$\\alpha_{iz}\; \mathrm{[1/m]}$", fontsize=fs)
        ax.set_xticklabels([])
    if i==3:
        ax = plt.subplot(gs[1,2:4])
        plt.plot(EField, Excitation, "*", markersize=ms, color="orange",  label="BOLSIG+")
        plt.plot(EField, Excitation, "-",  lw=lws, color="grey", label="Splin")
        plt.ylabel("$\\alpha_{ex}\; \mathrm{[1/m]}$", fontsize=fs)
        ax.set_xticklabels([])
    if i==4:
        ax = plt.subplot(gs[2,2:4])
        plt.plot(EField, IonizationSec, "*", markersize=ms,  color="orange",  label="BOLSIG+")
        plt.plot(EField, IonizationSec, "-",  lw=lws, color="grey", label="Splin")
        plt.ylabel("$\\alpha_{e1}\; \mathrm{[1/m]}$", fontsize=fs)
        plt.xlabel("$\epsilon \mathrm{[eV]}$", fontsize=fs)

    ax.yaxis.offsetText.set_fontsize(fs)
    plt.rcParams["mathtext.fontset"] = "cm"
    plt.rcParams["text.usetex"] =True
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    plt.xlim(0,150)
    plt.ylim(0,)
    plt.grid(color='grey', which="both",ls="--")
plt.show()
