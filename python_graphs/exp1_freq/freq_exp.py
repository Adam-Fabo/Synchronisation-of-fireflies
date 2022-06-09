import matplotlib.pyplot as plt
import numpy as np


# 3, 0.25, koef 0.02
# 6, 0.5,  koef 0.04
#12, 1,    koef 0.8
######################### order
file = open("order_3.txt")
lines = file.readlines()
order3 = []

for line in lines:
    line = line.strip()
    order3.append(list(map(float,line.split(" "))))

file = open("order_6.txt")
lines = file.readlines()
order6 = []

for line in lines:
    line = line.strip()
    order6.append(list(map(float,line.split(" "))))


file = open("order_12.txt")
lines = file.readlines()
order12 = []

for line in lines:
    line = line.strip()
    order12.append(list(map(float,line.split(" "))))


#0.02 koef
fig, axes = plt.subplots(nrows=1, ncols=3,figsize=(15,5))
axes[0].plot(order3[:8000])
axes[0].title.set_text("Gauss σ = 3, μ = 0.25")
axes[0].set_xlabel("Steps")
axes[0].set_ylabel("Orderliness")
axes[0].set_ylim(0,1)



axes[1].plot(order6[:8000])
axes[1].title.set_text("Gauss σ = 6, μ = 0.5")
axes[1].set_xlabel("Steps")
axes[1].set_ylabel("Orderliness")
axes[1].set_ylim(0,1)


#0.001 koef
axes[2].plot(order12[:8000])
axes[2].title.set_text("Gauss σ = 12, μ = 1")
axes[2].set_xlabel("Steps")
axes[2].set_ylabel("Orderliness")
axes[2].set_ylim(0,1)
fig.tight_layout()

plt.savefig('exp1_freq.eps', format='eps')
#plt.savefig('exp1_freq.svg')
plt.show()







