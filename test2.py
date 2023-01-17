#!/usr/bin/python3

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

r = 1.0

fig, ax = plt.subplots()

circle = patches.Circle(xy=(0, 0), radius=r, fill=False, ec='b')
rect = patches.Rectangle(xy=(-r, -r), width=2*r, height=2*r, fill=False, ec='k')

ax.add_patch(circle)
ax.add_patch(rect)

monte = []
dot_x = []
dot_y = []

for i in range(1000):
    x = random.uniform(-r,r)
    y = random.uniform(-r,r)
    dot_x.append(x)
    dot_y.append(y)
    m = ax.plot(dot_x, dot_y, ".", c='r')
    monte.append(m)

ani = animation.ArtistAnimation(fig, monte, interval=50, repeat=False)

ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.axis('scaled')

plt.show()
