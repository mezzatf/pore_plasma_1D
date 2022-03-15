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
vvv = 200  #choose the voltage you interested to plot its power density at different micro-gap sizes

#start_case index, #end_case index
start_file, end_file, TSim, RT = 321, 332, 882, 300
start_file, end_file, TSim, RT = 341, 352, 730, 100
start_file, end_file, TSim, RT = 361, 372, 672, 30

# wop = 2
# vvv = 500  #choose the voltage you interested to plot its power density at different micro-gap sizes
# start_file, end_file = 321, 372


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
lws = 4


if wop ==1:
    WTDic = {}
    PressureFile= os.path.expanduser('./PressureFile_%s.csv'%RT)


if wop ==2:
    plt.figure(figsize=(11,8))
    WTDic = {}
    PowerFile= os.path.expanduser('./PowerFile_%s.csv'%vvv)

for index, file in enumerate(np.arange(start_file, end_file+1)):

    #reading Zapdos output exdous file:
    filedir = os.path.expanduser("../code/zapdos/%03d-case/mean_en_out.e"%file)
    try:
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
                    if  t[i+1]*1e9 < TSim:
                         A += 0.5*(t[i+1]-t[i]) * (Wt[i+1]+Wt[i])


        #------------------------------------
        #plotting the power density optional
        #------------------------------------
            mark = ["-.*",  "--s", "-^"]
            lws  = 6
            if wop==2:
             #wop is argumnet you set when you run the python code.
                    if index <= 11:
                        Newindex = index
                    if 20<=index<=31:
                        Newindex = index%20
                    if 40<=index<=51:
                        Newindex = index%40

                    if vt[Newindex]== vvv and int(dv[Newindex]) == 10:
                        # print("Iam d = ", dv[index])
                        # print("Iam V = ", vt[index])
                        # plt.plot(t[index_start:]*1.e9, Wt[index_start:], "-", lw=lws, color="orange",  label="$d=$%3.0f $\mathrm{\mu}$"%(dv[index]))
                        # plt.yscale('linear')
                        # print(index, '%0.2E' %np.mean(Wt[index_start:]))
                        WW   = ["%0.3E" % member for member in Wt[index_start:]]
                        TT   = ["%010.6f" % member for member in t[index_start:]*1.e9]
                        if 321 <=file <=332:
                            Tr = 300
                        if 341 <= file <=352:
                            Tr = 100
                        if 361 <= file <=372:
                            Tr = 30
                        WTDic["W_%s_%s_%s"%(vvv,10,Tr)] = WW
                        WTDic["T_%s_%s_%s"%(vvv,10,Tr)] = TT
                        print('case=%s, VT=%s, Tr=%s, d=%s'%(file,vvv, Tr, dv[Newindex]))


                    if vt[Newindex]==vvv and int(dv[Newindex]) ==50:
                        # print("Iam d = ", dv[index])
                        # print("Iam V = ", vt[index])
                        # plt.plot(t[index_start:]*1.e9, Wt[index_start:], ":", lw=lws, color="green", label="$d=$%3.0f $\mathrm{\mu}$"%(dv[index]))
                        # print(index, '%0.2E' %np.mean(Wt[index_start:]))
                        WW   = ["%0.3E" % member for member in Wt[index_start:]]
                        TT   = ["%010.6f" % member for member in t[index_start:]*1.e9]
                        if 321 <=file<=332:
                            Tr = 300
                        if 341 <=file<=352:
                            Tr = 100
                        if 361 <=file<=372:
                            Tr = 30
                        WTDic["W_%s_%s_%s"%(vvv,50,Tr)] = WW
                        WTDic["T_%s_%s_%s"%(vvv,50,Tr)] = TT
                        print('case=%s, VT=%s, Tr=%s, d=%s'%(file,vvv, Tr, dv[Newindex]))


                    if vt[Newindex]==vvv and int(dv[Newindex]) ==100:
                        # print("Iam d = ", dv[index])
                        # print("Iam V = ", vt[index])
                        # plt.plot(t[index_start:]*1.e9, Wt[index_start:], "--", lw=lws,color="grey", label="$d=$%3.0f $\mathrm{\mu}$"%(dv[index]))
                        # print(index, '%0.2E' %np.mean(Wt[index_start:]))
                        WW   = ["%0.3E" % member for member in Wt[index_start:]]
                        TT   = ["%010.6f" % member for member in t[index_start:]*1.e9]
                        if 321 <=file<=332:
                            Tr = 300
                        if 341 <=file<=352:
                            Tr = 100
                        if 361 <=file<=372:
                            Tr = 30
                        WTDic["W_%s_%s_%s"%(vvv,100,Tr)] = WW
                        WTDic["T_%s_%s_%s"%(vvv,100,Tr)] = TT
                        print('case=%s, VT=%s, Tr=%s, d=%s'%(file,vvv, Tr, dv[Newindex]))


        #------------------------------------
        #calculate plasma pressure
        #------------------------------------
            if wop ==1:
                Eden.append(A)
                M_n = 14.0e-3                 #kg per mole (Nitrogen Atomic Mass)
                cv  = 5.0/2.0 * R /(M_n)      #Heat cpacity # R is the ideal gas constant
                tf  = 300.0 + A/(cv*1.225)    #calcaute plasma temerature
                p_i = 0.101325                #initial presure in MPa
                pf  = (tf/300.0)*p_i          # calculate the pressure
                print("File %s"%file)
                print("PF=%s"%pf)
                print("AA=%s"%A)
                if (file-start_file)<=3:
                    Vol = 4.0/3.0 * np.pi * (1e-5)**3
                    dE  = A * Vol * (20.0*1e-3*5.0)/(100.0*1e-5)
                    d10.append(pf)
                    W10.append(A)
                    dE10.append(dE)
                if 3<(file-start_file)<=7:
                    Vol = 4.0/3.0 * np.pi * (5e-5)**3
                    dE  = A * Vol * (20.0*1e-3*5.0)/(100.0*5e-5)
                    d50.append(pf)
                    W50.append(A)
                    dE50.append(dE)
                if 7<(file-start_file)<=11:
                    Vol = 4.0/3.0 * np.pi * (1e-4)**3
                    dE  = A * Vol * (20.0*1e-3*5.0)/(100.0*1e-4)
                    d100.append(pf)
                    W100.append(A)
                    dE100.append(dE)

    except:
      # print(filedir)
      print("%s isn't a case"%file)

# Collect the power data and insert it in the power_data directory
if wop == 1:
   WTDic["V_Max"]      = [200, 300, 400, 500]
   WTDic["P_%s"%(10)]  = d10
   WTDic["P_%s"%(50)]  = d50
   WTDic["P_%s"%(100)] = d100
   PressureDataFrame =pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in WTDic.items() ]))
   PressureDataFrame.to_csv(PressureFile, encoding='utf-8', index=False)

# Calculate the pressure and insert it in the pressure_data directory
if wop ==2: #wop is an argument to be set when running the code
    PowerDataFrame =pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in WTDic.items() ]))
    PowerDataFrame.to_csv(PowerFile, encoding='utf-8', index=False)
    print(Wt[index_start])
