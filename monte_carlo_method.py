#!/usr/bin/python3

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

points = 500

r = 1.0
in_circle = 0
out_circle = 0

fig = plt.figure()
ax1 = fig.add_subplot(121)

circle = patches.Circle(xy=(0, 0), radius=r, fill=False, ec='b')
rect = patches.Rectangle(xy=(-r, -r), width=2*r, height=2*r, fill=False, ec='k')

ax1.add_patch(circle)
ax1.add_patch(rect)

fig.text(0.3 ,0.8, 'Monte Carlo Method', fontsize='xx-large')

monte = []

dot_x = []
dot_y = []

for i in range(points):
    x = random.uniform(-r,r)
    y = random.uniform(-r,r)
    dot_x.append(x)
    dot_y.append(y)

    if pow(x,2)+pow(y,2) > 1:
        out_circle+=1
    elif pow(x,2)+pow(y,2) <= 1:
        in_circle+=1

    m = ax1.plot(dot_x, dot_y, ".", c='#4daf4a')

    text0 = ax1.text(1.3, 0.7, ("Total number of points : "+str(in_circle+out_circle)), size=15, color='b')
    text1 = ax1.text(1.5, 0.3, ("In a circle : "+str(in_circle)), size=15)
    text2 = ax1.text(1.5, -0.1, ("Out of circle : "+str(out_circle)), size=15)
    text3 = ax1.text(1.5, -0.6, (" PI = (4 * "+str(in_circle)+") / "+str(in_circle+out_circle)), size=18, color='r')
    text4 = ax1.text(1.9,-0.9, ("= "+str((4*in_circle)/(in_circle+out_circle))), size=18, color='r')
 
    monte.append(m + [text0] + [text1] + [text2] + [text3] + [text4])

ani = animation.ArtistAnimation(fig, monte, interval=20, repeat=False)

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)

ax1.axes.xaxis.set_visible(False)
ax1.axes.yaxis.set_visible(False)
ax1.set_aspect('equal')
plt.axis('scaled')

ani.save("monte_carlo_method.gif",writer='imagemagick')
plt.show()
