import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# LOAD file

file = open("fire_order.txt")
lines = file.readlines()
array = []
counter = -1
for line in lines:
    line = line.strip()
    # if not line:
    #     array.append([])
    #     counter+=1
    #     continue

    array.append(list(map(float,line.split(" "))))

array = np.array(array[:6000])
length = array.shape[0]
print(length)

fig, ax = plt.subplots(figsize=(8,8))
line, = ax.plot(array)



ax.set_ylabel('Orderliness')
ax.set_xlabel('Steps')
ax.set_title('Order in time')

def animate(i):
    print("Order: ", i, " of ", length)

    if i < 500:
        ax.set_xlim(left=0, right=i)
    else:
        ax.set_xlim(left=i-500, right=i)



ani = animation.FuncAnimation(fig, animate, frames=length-3, repeat=False, interval = 0.01)




# To save the animation, use e.g.
#
# writervideo = animation.FFMpegWriter(fps=60)
# ani.save('movie.mp4', writer=writervideo)
#ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)
#plt.title("Order in time")
plt.show()

# writervideo = animation.FFMpegWriter(fps=60)
# ani.save('final_order2.mp4', writer=writervideo,dpi=1000)

