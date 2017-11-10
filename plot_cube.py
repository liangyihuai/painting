# -*- coding: utf-8 -*
# 载入模块
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# 创建 3D 图形对象
fig = plt.figure()
ax = Axes3D(fig)

# 生成数据并绘制图 1
x1 = np.linspace(-3 * np.pi, 3 * np.pi, 500)
y1 = np.sin(x1)
ax.plot(x1, y1, zs=0, c='red')

# 生成数据并绘制图 2
x2 = np.random.normal(0, 4, 100)
y2 = np.random.normal(0, 4, 100)
z2 = np.random.normal(0, 4, 100)
ax.scatter(x2, y2, z2)

x = np.arange(-10, 10, 1)
y = np.arange(-10, 10, 1)
x, y = np.meshgrid(x, y)
R = np.sqrt(x**2 + x**2)
z = np.sin(R)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')

# 显示图
plt.show()