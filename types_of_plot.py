import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
print(x)

y = x**2
print(y)

plt.scatter(x,y)
plt.show()

plt.hist(y,x)
plt.show()


#  save the plot
fig = plt.figure(figsize = (8,8))  #means 800 X 800

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y)

plt.savefig("Basic.png")
