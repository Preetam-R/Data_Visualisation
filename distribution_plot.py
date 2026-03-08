import seaborn as sns
import matplotlib.pyplot as plt

dt = sns.load_dataset('tips')
print(dt)

print(dt['size'].unique())

#we can use subplots using plt

plt.subplot(1,2,1)
sns.histplot(dt['total_bill'], bins = 20)  #you can also control the bins in this graph

plt.subplot(1,2,2)
sns.histplot(dt['tip'])
plt.show()


# JOINT PLOT is used to compare the two data

sns.jointplot(x = 'total_bill', y = 'tip' , data = dt)
plt.show()


#  PAIR PLOT is used to anlyse the data

sns.pairplot(dt,hue = 'sex')  #hue divides the data into category (example is done for you)
plt.show()