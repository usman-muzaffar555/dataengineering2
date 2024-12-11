import pandas as pd

titanic_data = pd.read_csv("titanic.csv")


# print(titanic_data['Name'].head(100))

# split on the basis of some criteria and get the index
# print(titanic_data['Name'].str.split(",").str.get(0))

# get the length after split
print(titanic_data["Name"].str.split(",").str.len())

# get the first index after split and strip the values also
print(titanic_data["Name"].str.split(",").str[1].str.strip())

# get the split and add new column
print(titanic_data["Name"].str.split(",", expand=True))

print(titanic_data["Name"].str.contains("Owen"))

# replace value in the column
titanic_data['S-Sex'] = titanic_data['Sex'].replace({'male':'M', 'female':'F'})
print("short sex ", titanic_data['S-Sex'])

