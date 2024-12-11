import pandas as pd

data = pd.read_csv('titanic.csv')

#print(data)

ageSex = data[['Age', 'Sex']].groupby('Age')

print(ageSex.head(100))

ageSex2 = data[['Sex', 'Age']].groupby('Sex').count()


count = data['Sex'].value_counts()
print(count)

# number of person per cabin class

count = data['Pclass'].value_counts()

print(count)

print(data.groupby('Pclass')['Pclass'].value_counts())

print(data.groupby('Sex')['Sex'].value_counts())
print(data.groupby('Sex')['Sex'].size())