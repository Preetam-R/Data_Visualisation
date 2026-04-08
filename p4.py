import matplotlib.pyplot as plt

x = [0, 3, 3, 0, 0]
y = [0, 0, 2, 2, 0]

plt.plot(x, y)

plt.title("Rectangle")
plt.gca().set_aspect('equal')
plt.show()