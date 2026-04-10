import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 200)

r = 5 * np.sin(4 * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.title("Flower Pattern")
plt.gca().set_aspect('equal')
plt.show()