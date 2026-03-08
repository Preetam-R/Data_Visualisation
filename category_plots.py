import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

df = sns.load_dataset('tips')
print(df)

#  COUNT PLOT  
# count plot is used to count the categorical data in the dataframe

sns.countplot(x = df['sex'],hue = df['smoker'])
plt.show()

#  BAR PLOT  
#  bar plot needs two argumnets to be passed in the function.. 
#  _NOTE: x - axis = categorical values(qualitative values) , y - axis = distributive values (quantitave values)
# estimator are defualtly set on the basis on mean of the data [you can control the estimator]

sns.barplot(x = df['sex'] , y = df['tip'], estimator = np.max)
plt.show()


#  violinplot 

sns.violinplot(x = 'day', y = 'tip', data = df)
plt.show()

# STRIP PLOT

sns.stripplot(y = 'total_bill', x = 'day' , data = df)
plt.show()

#  SWARMPLOT

sns.swarmplot(x = 'day', y = 'total_bill' , data = df,hue = 'sex')
plt.show()