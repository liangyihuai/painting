# -*- coding: utf-8 -*-
"""
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, .1)
Y = np.arange(-4, 4, .1)
X, Y = np.meshgrid(X, Y)
Z = X*np.exp(-X**2 - Y**2)

# z = x * np.exp(-x ** 2 - y ** 2)

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()