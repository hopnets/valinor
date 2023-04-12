import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter
import statsmodels.api as sm
from statsmodels.graphics import tsaplots
import pandas as pd

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

font = {'family': 'sans-serif', 'size': 42}
font_label = {'family': 'sans-serif', 'size': 42}


plt.rc('font', **font)
plt.rc('legend', fontsize=36)


##### maps key to experiment name. modify as required ########
EXPERIMENT_MAP = {b'0': 'Cubic', b'2': 'Reno', b'3': 'vegas', b'4': 'BBR', b'1': 'DCTCP'}
#############################################################
legends = {b'0': 'Cubic', b'2': 'Reno', b'3': 'vegas', b'4': 'BBR', b'1': 'DCTCP'}
markers = {b'0': 'x', b'1':'s', b'2': '.', b'3': 'v', b'4': '<', b'5': '*', b'6': 'P', b'7': ''}
alphas = {b'0': 0.4, b'1':1, b'2': 0.4, b'3': 1, b'4': 0.4, b'5': 1, b'6': 0.4, b'7': 1}
linestyles = {b'0': 'solid', b'1':'dotted', b'2': 'dashed', b'3': 'dashdot', b'4': (0, (3, 1, 1, 1, 1, 1)), b'5': (0, (5, 10)), b'6': 'dotted', b'7': 'dashed'}

colors = ["lightskyblue", "navy", "dodgerblue", "black"]

case_index = 0
fig, ax1 = plt.subplots(figsize=(20,5))
# for experiment, ts_deltas_flows in queue_delta.items():
for experiment in [b'0', b'2', b'1', b'4']:
    if EXPERIMENT_MAP[experiment] == 'vegas':
        continue
    if EXPERIMENT_MAP[experiment] == 'Cubic':
        line_style = "dotted"
    elif EXPERIMENT_MAP[experiment] == 'Reno':
        line_style = "dashed"
    else:
        line_style = "solid"
    data = np.genfromtxt("sources/8_a_{}.csv".format(experiment), dtype=(float,float), delimiter=",")
    x, y = zip(*data)
    ax1.plot(x, y, label=EXPERIMENT_MAP[experiment], color=colors[case_index], linewidth=4, alpha=0.8, linestyle=line_style)
    ax1.set_facecolor('#f8f8f8')

    case_index += 1
ax1.set_ylabel(r"Delay ($\mu$s)")
ax1.set_xlabel("Time ($\mu$s)")
ax1.set_xticklabels(["", 0, 600, 1200, 1800, 2400, 3000])
for spine in ax1.spines.values():
    spine.set_visible(False)
ax1.grid(axis='y')
plt.legend(ncol=4, bbox_to_anchor=(-0.01,1,1,0.2), loc="center")

fig.patch.set_facecolor('#f8f8f8')
plt.savefig("presentation/8_a_w" + ".png", format='png', dpi=300, bbox_inches='tight')
