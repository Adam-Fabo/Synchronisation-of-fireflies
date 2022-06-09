import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors


file = open("fire_blik.txt")
lines = file.readlines()
array = []
counter = -1
for line in lines:
    line = line.strip()
    if not line:
        array.append([])
        counter+=1
        continue

    array[counter].append(list(map(float,line.split(" "))))

array = np.array(array[:6000])
length = array.shape[0]
print(length)

colormap = colors.LinearSegmentedColormap.from_list('custom blue', ['black','yellow'], N=256)

fig, ax = plt.subplots(figsize=(8,8))
ax.set()
i=1
im = plt.imshow(array[0], animated=True,cmap=colormap,aspect='auto', vmin=0, vmax=1)

#todo do frames/maxframes
def updatefig(*args):
    global i
    i+=1

    print("Fire: ", i, " of ", length)

    array[i] += array[i-1] - array[i-1]/10  # for blending purposes
    im.set_array(array[i])
    #ax.text(0.5, 1.100, "Frame: {:5d}/{}".format(i,length),
    #        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 5, 'edgecolor' : 'white'},
    #        transform=ax.transAxes, ha="center")
    return im,

ani = animation.FuncAnimation(fig, updatefig,frames=length-3, repeat=False, blit=True,interval = 0.1)
plt.show()

# toto ide iba na WSL
# writervideo = animation.FFMpegWriter(fps=60)
# ani.save('final_fire.mp4', writer=writervideo,dpi=1000)
