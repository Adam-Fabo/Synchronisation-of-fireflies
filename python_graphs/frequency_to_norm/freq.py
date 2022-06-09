import matplotlib.pyplot as plt
import numpy as np
import math
import random
from matplotlib.pyplot import figure

# prints fireflie blinking

koef = 0.07
nat_freq = 100*[3]

freq = [4.18]
for i in range(89):
    freq.append(freq[i]  +koef * (3 -freq[i]))


mod_freq = 10*[3]
mod_freq.extend(freq)
print(mod_freq)
plt.plot(nat_freq, label=" ω_nat")
plt.plot(mod_freq, label=" ω")
plt.plot([], [], ' ', label="ε = {}".format(koef))

plt.title("Firefly frequency with one stimuli")

plt.ylabel("Frequency [Hz]")
plt.xlabel("Steps")
plt.legend(loc="upper right")
#plt.savefig('.svg')
plt.savefig('freq_to_norm.eps', format='eps')
#plt.savefig('freq_to_norm.svg')
plt.show()

