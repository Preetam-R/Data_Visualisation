import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 100)

for r in range(1, 6):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y)

plt.title("Circle Pattern")
plt.gca().set_aspect('equal')
plt.show()
