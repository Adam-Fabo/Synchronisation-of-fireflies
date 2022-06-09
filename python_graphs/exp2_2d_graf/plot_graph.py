import subprocess
from subprocess import Popen, PIPE
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import os

low = 2
high = 39

# show data
a = []
for i in range(low,high):
    averages = np.fromfile('order_map_big_finale/order_test{}.dat'.format(i), dtype=float)
    a.append(averages)



fig, ax = plt.subplots(1,1)

img = ax.imshow(a)

x_label_list = ['A2', 'B2', 'C2', 'D2']

values = ["{}x{}".format(i,i) for i in range(low,high,2)]
ticks = list(range(low-2,high-2,2))

ax.set_xlabel("Coefficient")
ax.set_ylabel("Size")
ax.set_yticks(ticks)
ax.set_yticklabels(values)

xtick = [item for item in ax.get_xticks()]
xtick = np.float64(np.array(xtick))/100
print(xtick)

ax.set_xticklabels(xtick)



ax.title.set_text("Order with coeff ∈ <0.01,0.3>, step = 0.01")
# cbar = plt.colorbar(a)

cbar = fig.colorbar(img)
cbar.set_label('Orderliness',fontsize=12)

plt.savefig('exp1_2d.eps', format='eps')
#plt.savefig('exp1_2d.svg')
plt.show()
