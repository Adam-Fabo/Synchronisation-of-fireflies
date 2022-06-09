import matplotlib.pyplot as plt
import numpy as np
import math
import random
from matplotlib.pyplot import figure

# prints fireflie blinking


x = 3* list(range(0,100))
x.append(0)
plt.title("Firefly blinking with 100 step periode")

plt.plot(x,label="State of firefly")
plt.plot(100,100,'ro', label="Blink")
plt.plot(200,100,'ro')
plt.plot(300,100,'ro')

plt.ylabel("Firefly charge (%)")
plt.xlabel("Steps")
plt.legend(loc="upper left")
#plt.savefig('.svg')

plt.savefig('pilka.eps', format='eps')
#plt.savefig('pilka.svg')
plt.show()

