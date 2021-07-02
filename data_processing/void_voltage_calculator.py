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

######### capacitance_model ###################
#capacitance_model_voltage_calculator (c_model)
def void_cvoltage(v_t=400, d_e=20, phi=1, eps=5.58, d=10):
    phi  =  phi*1e-2
    d_e  =  d_e*1e-3      #m
    d    =  d*1e-6         #m
    d_t  =  d_e*phi        #m
    # v_PT =  v_t * eps * phi/(1.0 - phi + eps * phi)
    v_v  =  v_t*d*eps/d_e/(1.0 - phi + eps*phi)  #volt
    # v_q  =  v_t * (1.0 - phi)/(1.0 - phi + eps * phi)
    print("Void voltage = %s kV"%v_v)
    return v_t, d_e, d, v_v, phi

#looping for different voltages (c_model)
voltage_file  = os.path.expanduser("./voltages/c_voltage.csv")
voltage_file2 = os.path.expanduser("./voltages/c_voltage2.csv")

# f=open(voltage_file, "a+")
data = []
#j refers to the pulse peak voltage/
# you can vary the array according to Zapdos simulation
for j in np.array([200,300,400,500]):
    print (j)
    for i, d in enumerate(np.array([10,50,100])):
            v_t, d_e, d, v_v, phi = void_cvoltage(v_t=j, d_e=20, phi=1, eps=5.58, d=d)
            pi =  101325.0*1e-6  #MPA
            data_l = [v_t, d_e*1e3, d*1e6, v_v*1e3, phi, pi*d*1e6]
            data_l = ["%.2f" % member for member in data_l]
            data.append(data_l)
            print(data)

df = DataFrame(data, columns = ['vt', 'de', 'd', 'vv' , 'phi', 'pd'])
df2 = df.sort_values(by ='d')
print(df)
df.to_csv(voltage_file, encoding='utf-8', index=False)
df2.to_csv(voltage_file2, encoding='utf-8', index=False)

######### linear_model ###################
#linear_model_voltage_calculato (l_model)
def void_lvoltage(v_t=400, d_e=20, phi=5, eps=4, d=10):
    phi  =  phi*10e-3
    d_e  =  d_e*10e-4     #m
    d    =  d*1e-6     #m
    d_t  =  d_e*phi      #m
    v_v  =  v_t*d/d_e   #volt
    print("Void voltage = %s kV"%v_v)
    return v_t, d_e, d, v_v, phi

#looping for different voltages (l_model)
voltage_file= os.path.expanduser("./voltages/l_voltage.csv")
f=open(voltage_file, "a+")
data = []
for j in np.array([200,300,400,500]):
    print (j)
    for i, d in enumerate(np.array([10,50,100])):
            v_t, d_e, d, v_v, phi = void_lvoltage(v_t=j, d_e=20, phi=5, eps=4, d=d)
            pi =  101325.0*1e-6  #MPA
            data_l=[v_t, d_e*1e3, d*1e6, v_v*1e3, phi, pi*d*1e6]
            data_l = ["%.2f" % member for member in data_l]
            data.append(data_l)
            print(data)

df = DataFrame(data, columns = ['vt', 'de', 'd', 'vv' , 'phi', 'pd'])
df.to_csv(voltage_file, encoding='utf-8', index=False)

######### resistance_model ###################
#resistance_model_voltage_calculator (l_model)
def void_rvoltage(v_t=400, d_e=20, phi=5, eps=4, d=10):
    phi  =  phi*10e-3
    d_e  =  d_e*10e-4     #m
    d    =  d*1e-6     #m
    d_t  =  d_e*phi      #m
    v_v  =  v_t*d/(d_t)   #volt
    print("Void voltage = %s kV"%v_v)
    return v_t, d_e, d, v_v, phi

#looping for different voltages (r_model)
voltage_file= os.path.expanduser("./voltages/r_voltage.csv")
f=open(voltage_file, "a+")
data = []
for j in np.array([200,300,400,500]):
    print (j)
    for i, d in enumerate(np.array([10,50,100])):
            v_t, d_e, d, v_v, phi = void_rvoltage(v_t=j, d_e=20, phi=5, eps=4, d=d)
            pi =  101325.0*1e-6  #MPA
            data_l=[v_t, d_e*1e3, d*1e6, v_v*1e3, phi, pi*d*1e6]
            data_l = ["%.2f" % member for member in data_l]
            data.append(data_l)
            print(data)
df = DataFrame(data, columns = ['vt', 'de', 'd', 'vv' , 'phi', 'pd'])
df.to_csv(voltage_file, encoding='utf-8', index=False)
