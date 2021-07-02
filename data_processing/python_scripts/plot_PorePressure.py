import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

import numpy as np
gs = gridspec.GridSpec(1, 3)
fs  = 26 #font_size for the plot
ms  = 16 #marker_size
lws = 4

fig=plt.figure(figsize=(14,6))

for Trindex, Tr in enumerate([30,100,300]):
    PressureFile = os.path.expanduser('../pressure_data/PressureFile_%s.csv'%Tr)
    data =pd.read_csv(PressureFile, delimiter=",")
    ax = plt.subplot(gs[0, Trindex])

    if Trindex == 0 :
        plt.ylabel("$P_{P,f}$ [MPa]", fontsize=fs)
    else :
        plt.ylabel("")
        ax.set_yticklabels([])
    plt.yticks(fontsize=fs)

    plt.xlabel("$V_{T,Max}$ [kV]", fontsize=fs)
    plt.xticks([100, 200, 300, 400, 500, 600], rotation=45,fontsize=fs)


    colors  = ['grey', 'orange', 'green']
    lines   = ['-s', '--^', ':D']
    plt.title("$\\tau_R=%s \;ns$"%Tr, fontsize=fs)
    V_Max = data['V_Max']
    P10   = data["P_%s"%(10)]
    P50   = data["P_%s"%(50)]
    P100  = data["P_%s"%(100)]
    plt.plot([100,600], [6.3+0.1,6.3+0.1], '-', color='red', lw=lws, label='$P_{P,C}$')
    plt.plot(V_Max, P100, lines[0],  markersize=ms, lw=lws, color=colors[0], label="$d_P$ = 100 $\mu m$")
    plt.plot(V_Max, P50,  lines[1],  markersize=ms, lw=lws, color=colors[1], label="$d_P$ = 50 $\mu m$")
    plt.plot(V_Max, P10,  lines[2],  markersize=ms, lw=lws, color=colors[2],   label="$d_P$ = 10 $\mu m$")

    plt.grid(color='grey', which="both",ls="--")
    plt.xlim(100,600)
    plt.ylim(0,10)
    plt.rcParams["mathtext.fontset"] = "cm"
    plt.rcParams["text.usetex"] =True
    ax.yaxis.offsetText.set_fontsize(fs-2)
    ax.yaxis.set_offset_position('left')


    if Trindex==0 :
       plt.legend(loc=2, numpoints = 1)
fig.tight_layout()
fig.subplots_adjust(bottom=0.20)
#plt.savefig("./power/Power.eps")
plt.show()


#
# ax = pl.subplot(gs[0, 0]) # row 0, col 0
# pl.plot([0,1])
#
# ax = pl.subplot(gs[0, 1]) # row 0, col 1
# pl.plot([0,1])
#
# ax = pl.subplot(gs[1, :]) # row 1, span all columns
# pl.plot([0,1])
