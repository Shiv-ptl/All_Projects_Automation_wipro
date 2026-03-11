import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("flights")

#lineplot
sns.lineplot(x='year',y='passengers',data=data)
plt.title('yearly passengers growth')
plt.show()


#bar plot
data = sns.load_dataset("tips")
sns.barplot(x= 'day',y='total_bill',data=data)
plt.title("Avg bills per day")
plt.show()

#scatterplot
data = sns.load_dataset("tips")
sns.scatterplot(x= 'total_bill',y='tip',data=data)
plt.title("Avg tips per day")
plt.show()

#histogram
data = sns.load_dataset("tips")
sns.histplot(data['total_bill'],bins=20)
plt.title("total bill vs tips")
plt.show()

#boxplot
data = sns.load_dataset("tips")
sns.boxplot(x='day',y= 'total_bill',data=data)
plt.title("Bill distribution by day")
plt.show()

#heat map
data=sns.load_dataset("tips")
corr = data.corr(numeric_only=True)

sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Coorelation heatmap")
plt.show()

#pair plot
data = sns.load_dataset("iris")
sns.pairplot(data)
plt.show()

#violin Plot
data = sns.load_dataset('tips')
sns.violinplot(x='day',y='total_bill',data=data)
plt.title("Bill Distribution by Day")
plt.show()
#count plot
data = sns.load_dataset('tips')
sns.countplot(x='day',data=data)
plt.title("Number of customer per Day")
plt.show()



#Regression Plot
data = sns.load_dataset("tips")
sns.regplot(x="total_bill",y= "tip",data=data)
plt.title("Regression between Bill and Tip")
plt.show()

