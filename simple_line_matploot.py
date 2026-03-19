import matplotlib.pyplot as plt

for i in range(10):
    plt.plot([0, i], [i, 10], marker='o')

plt.title("Line Design Pattern")
plt.show()
