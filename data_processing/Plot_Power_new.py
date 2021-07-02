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

wop = 1
vvv = 500  #choose the voltage you interested to plot its power density at different micro-gap sizes

#start_case index, #end_case index
#start_file, end_file = 321, 332
#start_file, end_file = 341, 352
#start_file, end_file = 361, 372

wop = 2
vvv = 500  #choose the voltage you interested to plot its power density at different micro-gap sizes
start_file, end_file = 321, 372


wop = int(wop)

#------------------------------------
#empty lists to collect plamsa pressure
#------------------------------------
d10  = []  #10 microns gap pressures at 200, 300, 400 and 500 kV
d50  = []  #50 microns gap pressures at 200, 300, 400 and 500 kV
d100 = []  #100 microns gap pressures at 200, 300, 400 and 500 kV

W10  = []  #10 microns gap pressures at 200, 300, 400 and 500 kV
W50  = []  #50 microns gap pressures at 200, 300, 400 and 500 kV
W100 = []  #100 microns gap pressures at 200, 300, 400 and 500 kV


#------------------------------------
#empty lists to collect energy
#------------------------------------
dE10  = []  #10 microns gap energies at 200, 300, 400 and 500 kV
dE50  = []  #50 microns gap energies at 200, 300, 400 and 500 kV
dE100 = []  #100 microns gap energies at 200, 300, 400 and 500 kV
Eden  = []  #All energy densities

#------------------------------------
#read voids voltages
#------------------------------------
voltage_file = os.path.expanduser('./voltages/c_voltage2.csv')
data =pd.read_csv(voltage_file, delimiter=",")
heads=list(data.columns)
vt=data[heads[0]]
dv=data[heads[2]]




fs  = 26 #font_size for the plot
ms  = 16 #marker_size
lws = 6


for index, file in enumerate(np.array([332,372])):
    print(index)
    #reading Zapdos output exdous file:
    filedir = os.path.expanduser("../code/zapdos/%03d-case/mean_en_out.e"%file)
    f = open(filedir)
    # print("index= ",index)
    dataset = Dataset(filedir)
    varkeys = list(dataset.variables.keys())
    #reading the simulation domain
    X  = dataset.variables[varkeys[31]]  #[m]
    t  = dataset.variables[varkeys[0]]

    Wt_1D = []  #empty list to collect the 1D power density
    for i in range(len(t)):
        W = dataset.variables[varkeys[42]][i]
        Wt_1D.append(np.mean(W))

    Wt = 3.0 * np.array(Wt_1D) #generalize 1D to 3D according to Kinetic theory
    index_start = 0            #lower integeration limit
    index_end   = len(t) -1    #higher integeration limit

    #Integerate the power density to calculate the energy density (trapezoid approach)
    if wop ==1:
        A  = 0
        for i in np.arange(index_start, index_end):
            A += 0.5*(t[i+1]-t[i]) * (Wt[i+1]+Wt[i])


#------------------------------------
#plotting the power density optional
#------------------------------------
    mark = ["-.*",  "--s", "-^"]
    lws  = 6
    if wop==2:



                plt.plot(t[index_start:]*1.e9,Wt[index_start:])

plt.show()
