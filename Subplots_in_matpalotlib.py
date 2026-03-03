import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(0,5,11)
print(x)

y = x**2
print(y)

#  so what do subplot does
 #subplot takes 3 arguments 1.number of rows 2.number of columns 3.plot number which u want to plot the graph

#the subplots shows mupltiple plots on the one single plot

plt.subplot(2,2,1)  #first block
plt.xlabel("boys")
plt.ylabel("girls")   #you can also modify by giving labels to it 
plt.plot(x,y)
plt.show()

plt.subplot(2,2,2)  #second block
plt.plot(y,x)
plt.show()

plt.subplot(2,2,3)  # third block
plt.plot(x**2,y**2)
plt.show()

plt.subplot(2,2,4)  #fourth block
plt.plot(x*2,y**4)
plt.show()



