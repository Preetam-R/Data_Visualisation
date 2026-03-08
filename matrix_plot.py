import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#  HEATMAP is based on the covarience

tips = sns.load_dataset('tips')
print(tips)

tipss = tips[['total_bill','tip','size']]
print(tipss)

tipscorr = tipss.corr()
print(tipscorr)

sns.heatmap(tipscorr,annot = True)
plt.show()


# PIVOT TABLE  
print()
fly = sns.load_dataset('flights')
print(fly)

pvt = fly.pivot_table(values = 'passengers', index = 'month', columns = 'year' )
print(pvt)

sns.heatmap(pvt)
plt.show()
