import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips)
print()

sns.lmplot(data = tips, x = 'total_bill', y = 'tip', hue = 'sex')
plt.show()