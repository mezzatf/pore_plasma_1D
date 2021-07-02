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
import scipy.ndimage

import matplotlib.gridspec as gridspec
select = 3
fs = 26
if select == 6:
    gs = gridspec.GridSpec(2,3)

    phi = np.arange(0,0.201,0.001)
    dp  = np.arange(0,1001,1)*1e-6

    eps = 5.58

    P, D = np.meshgrid(phi,dp)

    fig = plt.figure(figsize=(12,8))

    plt.xlim(0,20)
    plt.ylim(0,1000)

    for i, eps in enumerate(np.arange(4,10,1)):
        if  i < 3:
            j=0
            k=i
            ax = plt.subplot(gs[j,k])
            ax.set_xticklabels([])
        else:
            j=1
            k=i-3
            ax = plt.subplot(gs[j,k])
            ax.set_xlabel('$\phi \mathrm[\%]$')
        if k>0:
            ax.set_yticklabels([])
        else:
            ax.set_ylabel('$d_P \mathrm[\mu m]$')
        F  = D * eps / (1 - P + eps*P)
        plt.title("$\\varepsilon=%s$"%eps)
        plt.pcolormesh(P*100,D*1e6,F, cmap="hsv", vmin=0, vmax=0.006, shading='auto')

    fig.subplots_adjust(bottom=0.25)
    cbaxes = fig.add_axes([0.1, 0.1, 0.8, 0.03])
    cb = plt.colorbar(cax = cbaxes, orientation='horizontal')
    plt.show()

if select == 3:
    gs = gridspec.GridSpec(1,3)

    phi = np.arange(0,0.101,0.001)
    eps = np.arange(4,10.01,0.01)
    #dp  = np.arange(0,1001,1)*1e-6

    # eps = 5.58

    P, EPS = np.meshgrid(phi,eps)

    fig = plt.figure(figsize=(13,4.5))

    dE = 20*1e-3
    for i, D in enumerate(np.array([10, 50, 100])):
        j = 0
        k = i
        if i == 0:
            m=3
        if i == 1:
            m=2
        if i == 2:
            m=2

        ax = plt.subplot(gs[j,k])
        if k > 0:
            ax.set_yticklabels([])
        else:
            ax.set_ylabel('$\\varepsilon_G \mathrm[-]$', fontsize=fs)
        ax.set_xlabel('$\phi \mathrm[\%]$', fontsize=fs)

        F  = D*1e-6  * EPS / (1 - P + EPS*P) / dE
        plt.title("$d_P=%s\; \mathrm{\mu m}$"%(D), fontsize=fs)
        print(i, D)
        print(F.min(), F.max())
        plt.pcolormesh(P*100, EPS, F, cmap="hsv", vmin= F.min(), vmax= F.max() ,shading='auto')
        plt.xticks([0,5,10], fontsize=fs)
        plt.yticks([4,6,8,10], fontsize=fs)

        if k<2:
            cb = plt.colorbar()
            cb.ax.tick_params(labelsize=fs)
        if k==2:
            cb = plt.colorbar()
            cb.set_label("$V_P/V_T \; \mathrm{[kV/kV]}$", fontsize=fs-4)
            cb.ax.tick_params(labelsize=fs)

        plt.rc('font', size=fs)
        cb.set_ticks(np.linspace(round(F.min(),m), round(0.9 *F.max(),m), 3))
        cb.formatter.set_powerlimits((0, 0))
        cb.ax.yaxis.set_offset_position('left')
        cb.ax.yaxis.get_offset_text().set_fontsize(fs)



        #
        #     cbar=plt.colorbar()
        #     cbar.set_label("$d_{P,Eff}\; \mathrm{[\mu m]}$")
        #     cbar.formatter.set_powerlimits((0, 0))
        #     cbar.ax.yaxis.set_offset_position('right')
        #     cb.update_ticks()

    fig.subplots_adjust(bottom=0.25)
    # cbaxes = fig.add_axes([0.9, 0.15, 0.02, 0.72])
    # cb = plt.colorbar(im, cax = cbaxes)
    # cb.set_label("$d_{P,Eff}\; \mathrm{[\mu m]}$")
    # cb.formatter.set_powerlimits((0, 0))
    plt.show()
