import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread('virat.jpg')
print(img)
plt.imshow(img)
plt.axis('off')   # optional (removes axis)
plt.show()
