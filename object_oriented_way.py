import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
print(x)

y = x**2
print(y)

fig = plt.figure(figsize = (8,8))  #means 800 X 800

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y)

axes2 = fig.add_axes([0.4,0.6,0.3,0.3])   # smaller second axes
axes2.plot(x,y)

plt.show()
#so basically you have the control on the canvas
