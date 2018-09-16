#!/usr/local/lib
# -*- coding: UTF-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import matplotlib.style
# import matplotlib as mpl
matplotlib.style.use('classic')

n_groups = 4

data = [[44,43,45,44,45,44,46,48],[452,389,363,394,395,404,459,372],[755,643,659,586,759,596,608,606], [1150,1065,1269,1061,1085,1094,1168,1183]]

means_men = (np.mean(data[0]),np.mean(data[1]),np.mean(data[2]),np.mean(data[3]))
std_men = (np.std(data[0], ddof = 1),np.std(data[1], ddof = 1),np.std(data[2], ddof = 1),np.std(data[3], ddof = 1))


fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.40

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, means_men, bar_width,
                alpha=opacity, color='red',
                yerr=std_men)

# rects2 = ax.bar(index + bar_width, means_women, bar_width,
#                 alpha=opacity, color='gray',
#                 yerr=std_women, error_kw=error_config,
#                 label="UniGL")

ax.set_xlabel('Concurrent Threads')
ax.set_ylabel('Execution Time (us)')
ax.set_title('Time Plot (key_max = 50, iters = 20)')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('1', '2', '4', '8'),ha='center')
# ax.legend()

fig.tight_layout()
# plt.show()
plt.savefig('plot.png', format='png', dpi=1000)
