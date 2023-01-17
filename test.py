#!/usr/bin/python3

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

r = 1.0

monte = []

fig = plt.figure()
ax = plt.axes()

circle = patches.Circle(xy=(0, 0), radius=r, fill=False, ec='b')
rect = patches.Rectangle(xy=(-r, -r), width=2*r, height=2*r, fill=False, ec='k')

ax.add_patch(circle)
ax.add_patch(rect)

'''
for i in range(100):
    dot_x = random.uniform(-r,r)
    dot_y = random.uniform(-r,r)
    m = ax.plot(dot_x, dot_y, ".")
    monte.append(m)

'''

def monte(data):
    dot_x = random.uniform(-r,r)
    dot_y = random.uniform(-r,r)
    ax.plot(dot_x, dot_y, ".")


ani = animation.FuncAnimation(fig, monte, interval=100, , repeat=False)

ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.axis('scaled')

plt.show()
