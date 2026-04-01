"""epochs = [1,2,3,4,5]
train_loss = [0.9,0.6,0.5,0.4,0.35]
val_loss = [1.0,0.7,0.6,0.5,0.45]
plt.plot(epochs,train_loss,label="Train Loss")
plt.plot(epochs,val_loss,label = "Validation Loss")
plt.title("Loss v/s Epochs")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

#for bar chart
classes = ['Setose','Versicolor','Virginica']
counts = [30,50,20]
plt.bar(classes,counts)
plt.title("Class Distribution in Iris Dataset")
plt.ylabel('Number of Samples')
plt.show()

#for histogram
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("iris")
plt.hist(df['petal_length'], bins=5)
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df['sepal_length'], df['petal_length'], 
            c=df['species'].astype('category').cat.codes)
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Scatter: Sepal vs Petal Length')
plt.show() 

import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset("titanic")

# Uncomment to use countplot

sns.countplot(x="survived", data=df)
plt.title("Survival Distribution")
plt.xlabel("Survived (0=No, 1=Yes)")
plt.ylabel("Count")
plt.show()


# Boxplot of Age distribution by Survival status
sns.boxplot(x='survived', y='age', data=df)  
plt.title("Age Distribution by Survival")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Age")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("titanic")

sns.violinplot(x="pclass",y="fare",hue="survived",split=True,data=df)
plt.title("Fare Distribution by Pclass and Survival")
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title("Feature Correlation")
plt.show()"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')
df.tail()