import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x, y = np.mgrid[-1:1:20j, -1:1:20j]
z = x * np.exp(-x ** 2 - y ** 2)

ax = plt.subplot(111, projection='3d')
ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plt.cm.coolwarm, alpha=0.8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()