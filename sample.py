#!/usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()
line = ax.plot([], [])

def gen_function():
    y = [0] * 30
    x = range(len(y))
    for _x, _y in zip(x, y):
        yield [_x, _y]

def init():
    ax.set_xlim(0, 30) # x軸固定
    ax.set_ylim(-1, 1) # y軸固定
    del (x_data[:], y_data[:]) # データを削除
    return line

def plot_func(frame):
    x_data.append(frame[0])
    y_data.append(frame[1])
    line.set_data(x_data, y_data) # 繰り返しグラフを描
    return line

anim = FuncAnimation(fig=fig, func=plot_func, frames=gen_function, init_func=init, interval=100)

plt.show()
