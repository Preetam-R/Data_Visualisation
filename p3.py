import matplotlib.pyplot as plt

labels = ['A', 'B', 'C']
sizes = [30, 50, 20]

plt.pie(sizes, labels=labels)

plt.title("Pie Chart")
plt.show()