import matplotlib.pyplot as plt
import numpy as np


######################### order
file = open("good_order.txt")
lines = file.readlines()
good_order = []

for line in lines:
    line = line.strip()
    good_order.append(list(map(float,line.split(" "))))

file = open("bad_order.txt")
lines = file.readlines()
bad_order = []

for line in lines:
    line = line.strip()
    bad_order.append(list(map(float,line.split(" "))))

file = open("big_order.txt")
lines = file.readlines()
big_order = []

for line in lines:
    line = line.strip()
    big_order.append(list(map(float,line.split(" "))))



fig, axes = plt.subplots(nrows=1, ncols=3,figsize = (15,5))

#0.002 koef
axes[0].plot(bad_order[:6000])
axes[0].title.set_text("Not synced fireflies, coeff = 0.002")
axes[0].set_xlabel("Steps")
axes[0].set_ylabel("Orderliness")
axes[0].set_ylim(0,1)



#0.02 koef
axes[1].plot(good_order[:6000])
axes[1].title.set_text("Synced fireflies, coeff = 0.02")
axes[1].set_xlabel("Steps")
axes[1].set_ylabel("Orderliness")
axes[1].set_ylim(0,1)

#0.2 koef
axes[2].plot(big_order[:6000])
axes[2].title.set_text("Unstable fireflies, coeff = 0.2")
axes[2].set_xlabel("Steps")
axes[2].set_ylabel("Orderliness")
axes[2].set_ylim(0,1)
fig.tight_layout()
plt.savefig('order.eps', format='eps')

plt.show()






