#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 7 16:00:00 2020
-------------------------------------
ETH-Zurich
Geothermal Energy and Gefluids Group
Plasma pulse drillig doctoral projects
Professor Martin Saar
Dr Benjamin Adams & Dr Daniel Vogler
Doctoral candidate: Mohamed Ezzat
Email: m.Ezzat@erdw.ethz.ch
------------------------------------
This script to calculate the effective relative
of the rock knowing the relative permittivity
and the volume fraction of its compositions.
------------------------------------
Granite compositions
---------------------
Mineral & Volume fraction & $\varepsilon$ & Reference \\
\hline
K-feldspare & 45\% & 6.03 & \citep{Nelson1989} \\
Plagioclase & 20\% & 6.34 & \citep{Zheng_2005}    \\
Quartz      & 30\% & 4.5  & \citep{Stuart_1955} \\
Biotite     & 5\% &  6.30 & \citep{Olhoeft_1979} \\
\hline
"""
#------------------------------------
#Required libraries
#------------------------------------
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os
from pandas import DataFrame

RP = np.array([6.03, 6.34, 4.5, 6.30])
VF = np.array([45, 20, 30, 5]) #%


Eff = np.sqrt(sum(RP*VF)/sum(VF/RP))
print(Eff)
