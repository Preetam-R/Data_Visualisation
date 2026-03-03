import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#lets create an array
x = np.linspace(0,5,11)
print(x)

# lets create another array

y = x**2
print(y)

#now we have x and y lets plot these array

pl = plt.plot(x,y)
#now lets add title and labels to the our plot
plt.title("School_stats")
plt.xlabel("CLass")
plt.ylabel("Students")

plt.show()  # this is used to show the plotted 

