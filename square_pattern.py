import matplotlib.pyplot as plt

for i in range(5):
    plt.plot([i, i, 5-i, 5-i, i],
             [i, 5-i, 5-i, i, i])

plt.title("Square Pattern")
plt.gca().set_aspect('equal')
plt.show()
