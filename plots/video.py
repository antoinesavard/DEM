import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from files import *
import os

output_dir = "output/"
expno = "01"

filesx = list_files(output_dir, "x", expno)
filesy = list_files(output_dir, "y", expno)
filesr = list_files(output_dir, "r", expno)
filesh = list_files(output_dir, "h", expno)

xdata, ydata, radii, mass = (
    multiload(output_dir, filesx),
    multiload(output_dir, filesy),
    multiload(output_dir, filesr),
    multiload(output_dir, filesh),
)

os.chdir("plots/")

fig = plt.figure(dpi=300, figsize=(4, 4))
ax = fig.add_axes([0.14, 0.14, 0.8, 0.8])

time = ax.text(0.02, 0.95, "", transform=ax.transAxes)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

disks = []


def init():
    for i in range(len(radii[-1])):
        p = np.array([xdata[0, i], ydata[0, i]])
        disk = draw(ax, p, radii[0, i])
        disks.append(disk)
    time.set_text("")
    return disks


def animate(i):
    for j, disk in enumerate(disks):
        p = np.array([xdata[i, j], ydata[i, j]])
        disk.center = p
    time.set_text("iteration = {}".format(i))
    return disks


anim = FuncAnimation(
    fig,
    animate,
    frames=xdata.shape[0],
    init_func=init,
    interval=10,
    repeat=False,
    blit=True,
)

save_or_show_animation(anim, 1)
