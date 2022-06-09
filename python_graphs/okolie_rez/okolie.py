import matplotlib.pyplot as plt
import numpy as np

from matplotlib.pyplot import figure


def func(r):
    return 1/r

low = -5
high = 5
step = 0.01
r = np.arange(low,high,step)
r = 1/abs(r)
r[r > 1] = 1

y = []

x = np.arange(low,high+0.5,0.5)
for i in x:
    if int(i) == 0:
        y.append(1)
        continue
    print(1/abs(i))
    a = 1/abs(i)
    y.append(1/abs(int(i)))


x = np.arange(low,high,step)
y = np.array(1/np.abs(np.round(x)))
y[y > 1] = 1

x = x+5
x = x*100

print("y = ", y)
print("x = ", x)

plt_1 = plt.figure(figsize=(10, 8))

plt.title("Cut trough inverse law function at x-axis")
plt.xticks(np.arange(0,1000,50),np.arange(-5, 5, 0.5))
plt.plot(r, label = "Inverse law function")
plt.plot(x,y,label = "CA proximity function")


for i in np.arange(-4, 5, 1):
    if i == 4:
        plt.plot((i+5)*100,(1/np.abs(np.round(i))),"ro",label = "Sampling point")
    else:
        plt.plot((i+5)*100,(1/np.abs(np.round(i))),"ro")


plt.grid()
plt.legend(loc = 'upper left')
plt_1.savefig('okolie.svg')
plt.show()
