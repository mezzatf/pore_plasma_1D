import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

import numpy as np
gs = gridspec.GridSpec(3, 4)
fs  = 26 #font_size for the plot
ms  = 16 #marker_size
lws = 4

Tr = 30 #ns
fig=plt.figure(figsize=(12,8))


PlasmaTimeFile= os.path.expanduser('../voltages/PlasmaTimeFile.csv')
PlasmaTimeData = pd.read_csv(PlasmaTimeFile, delimiter=",")

TD = [678, 730, 882]
for Trindex, Tr in enumerate([30,100,300]):
    # PlasmaTime = list(PlasmaTimeData.iloc[Trindex])

    for index, VT in enumerate([200,300,400,500]):
        PowerFile = os.path.expanduser('../power_data/PowerFile_%s.csv'%VT)
        data =pd.read_csv(PowerFile, delimiter=",")
        ax = plt.subplot(gs[Trindex, index])
        if Trindex==2 :
            plt.xlabel("$t\; \mathrm{[ns]}$", fontsize=fs)
        if index == 0 and Trindex==1:
            plt.ylabel("$W_{Dep}\; \mathrm{\; [W/m^3]}$", fontsize=fs)
        # if Trindex ==0:
        #     ax.set_title("$V_{T,Max}$ = %s kV"%VT, fontsize=fs)
        if index >0 or Trindex ==0 or Trindex==2:
            ax.set_yticklabels([])
        if Trindex == 0:
            #ax.set_xticklabels([])
            plt.xticks([0, 250, 500, TD[Trindex],  1000], ["", "", "", "%s"%(TD[Trindex]), ""], fontsize=fs)
        if Trindex == 1:
            #ax.set_xticklabels([])
            plt.xticks([0, 250, 500, TD[Trindex-1], TD[Trindex],  1000], ["", "", "", "", "%s"%(TD[Trindex]), ""],  fontsize=fs)
        if Trindex == 2:
            plt.xticks([0, 250, 500, TD[Trindex-2], TD[Trindex-1], TD[Trindex],  1000], ["0", "250", "500", "", "", "%s"%(TD[Trindex]), ""], rotation=45, fontsize=fs)


        colors  = ['grey', 'orange', 'green']
        lines = ['-', '--', ':']
        for dindex, d in enumerate([100, 50, 10]):
            T     = data['T_%s_%s_%s'%(VT,d,Tr)]
            W     = data['W_%s_%s_%s'%(VT,d,Tr)]
            Label = "$d_p$=%s $\mathrm{\mu m}$"%(d)
            if dindex == 2:
                plt.axvspan(0, TD[Trindex], facecolor='cyan', alpha= 0.1)
            W_D = []
            T_D = []
            for it, t in enumerate(T):
                 if t <= TD[Trindex]:
                    T_D.append(T[it])
                    W_D.append(W[it])
            T_D.append(TD[Trindex])
            T_D.append(TD[Trindex])
            W_D.append(W_D[-1])
            W_D.append(0)

            plt.plot(T_D,W_D, lines[dindex],  lw=lws, color=colors[dindex], label=Label)
            PlasmaTime = PlasmaTimeData['V=%s_%s'%(VT,d)]
            #plt.vlines(PlasmaTime[Trindex], 0,1e14, color=colors[dindex])
            plt.grid(color='grey', which="both",ls="--")
            plt.xlim(0,1000)
            plt.ylim(0,0.9e14)
            plt.yticks([0,5e13], fontsize=fs)
            plt.rcParams["mathtext.fontset"] = "cm"
            plt.rcParams["text.usetex"] =True
            ax.yaxis.offsetText.set_fontsize(fs-2)
            ax.yaxis.set_offset_position('left')

            plt.rc('font', size=fs-10)
            plt.grid(color='grey', which="both",ls="--")
            if Trindex == 0 and index == 0:
                plt.text(500, 11*1e13, '$V_{T,Max} =$%s kV'%VT,
                         horizontalalignment='center',
                         verticalalignment='top',
                         multialignment='center',
                         fontsize=fs
                        )
            if Trindex == 0 and index > 0:
                plt.text(500, 11*1e13, '%s kV'%VT,
                         horizontalalignment='center',
                         verticalalignment='top',
                         multialignment='center',
                         fontsize=fs
                        )
            if index ==3:
                plt.text(1105, 4.5*1e13, '$\\tau_R =$%s ns'%Tr,
                         rotation=90,
                         horizontalalignment='center',
                         verticalalignment='center',
                         multialignment='center',
                         fontsize=fs
                        )

        if index==0 and Trindex==0 :
            plt.legend(loc=1,  numpoints = 1)

fig.subplots_adjust(bottom=0.15)
plt.savefig("../Figures/PowerDepDensity.png")
plt.show()
