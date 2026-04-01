#File I/O 
#Text Files: .txt,.docx,.log etc
#Binary Files: .mp4,.mov,.png,.jpeg etc

"""f = open("demo.txt","w")"""
"""data = f.read()
f.write("I want to learn javascript tommoore.123")
line1 = f.readline()
print(data)
print(line1)
print(type(data))
f.close()
# With Syntax
with open("demo.txt","a") as f:
    data = f.read()
    print(data)

#for deleting
import os
os.remove("demo.txt")
import pandas as pd
import numpy as np
# 2-item Series with matching index length
pd_series_1 = pd.Series([[75,92,88], [66,49,99]], index=['Maths', 'Biology'])
print("Maths scores in Series:")
print(pd_series_1['Maths'])

# 2-row DataFrame (this is fine and already correct)
pd_dataframe_1 = pd.DataFrame({ 
    'student_name': ['Shambhavi', 'Kiki'],
    'maths_score': [99, 98],
    'biology_score': [98, 99],
    ' Cs_score': [78, 76]
})

print("\nDataFrame first few rows:")
print(pd_dataframe_1.head()['student_name'].iloc[0])  # Correct

np_array1 = np.array([1,2,3,4])
pd_series1 = pd.Series([1,2,3,4])
print(pd_series1[1])
print(np_array1)

pd_series2 = pd.Series([[75,92,88], [66,49,99]], index=['Maths', 'Biology'])
print(pd_series2['Maths'])

dict1 = {'Maths': 75,'Biology':92,'CS':88}
pd_series3 = pd.Series(dict1)
print(pd_series3['Maths'])
print(pd_series3[0])

pd_series4 = pd.Series([1,2,3,4])

pd_series5 = pd_series4*2
pd_series6 = pd_series4 + 4

print(pd_series5)
print(pd_series6)
print(pd_series6.mean())

df1 = pd.DataFrame({'Name':['Shambhavi','Singh','heheh'],
                    'City':['Delhi','Roorkee','Hapur'],
                    'Height': [166,168,169]
                    })
print(df1['Name'])

import pandas as pd
import numpy as np

data_set = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print(data_set.head())
print(data_set.describe())
print(data_set['sepal_length'].head())
print(data_set[(data_set['sepal_length']>6)&(data_set['species'] =='setosa')])
data_set['sepal_ratio'] = data_set['sepal_length']/data_set['sepal_width']
print(data_set.head())
print(data_set.isnull().sum())
data_set.groupby('species')['sepal_width'].agg(['mean','min','max'])
data_set.sort_values(by='sepal_length',ascending=False)


import pandas as pd
import numpy as np
df1 = pd.DataFrame({'id':[1,2,3],'Name':['Alice','Bob','Nick']})
df2 = pd.DataFrame({'id':[1,2,3],'Score':['60','75','32']})
df3 = pd.DataFrame({'id':[4,5,6],'Name':['Shambhavi','Singh','kiki']})
df4 = pd.merge(df1,df2,on='id')
df5 = pd.concat([df1,df3],ignore_index=True)
print(df5)

import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)
print(titanic.head())
print(titanic.tail())
print(titanic.info())
print(titanic.describe())
print(titanic.isnull().sum())
print(titanic.isnull())
print(titanic['Age'].fillna(titanic['Age'].mean(),inplace=True))
print(titanic.info())
print(titanic.drop('Cabin',axis=1,inplace=True))
print(titanic.info())
print(titanic['Survived'].mean()*100)
print(titanic.info())
print(titanic.groupby('Sex')['Survived'].mean()*100)
print(titanic.groupby('Pclass')['Survived'].mean()*100)
print(titanic[titanic['Survived']==1].sort_values(by='Age',ascending=False))"""
import pandas as pd

dataset = pd.read_excel("E:\\internship1 project\\latest_dataset_employee_prediction.xlsx")
print(dataset.head(10))
print(dataset.shape)
print(dataset.isnull().sum())
print((dataset.isnull().sum()/dataset.shape[0])*100)