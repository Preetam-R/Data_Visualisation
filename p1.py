import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(0, 10*np.pi, 500)

x = np.cos(t)
y = np.sin(t)
z = t

ax.plot(x, y, z)

ax.set_title("3D Helix")
plt.show()