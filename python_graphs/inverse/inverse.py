import matplotlib.pyplot as plt
import numpy as np
import math
import random
from matplotlib.pyplot import figure

# prints fireflie blinking




def f(x, y):
    return 1/np.sqrt(x ** 2 + y ** 2)

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

Z[Z > 1] = 1
#print(type(Z))
fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='binary')

inv = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('Inverse square law - capped at 1')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
fig.colorbar(inv)

plt.savefig('inverse.svg')
plt.show()