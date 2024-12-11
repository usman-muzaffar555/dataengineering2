import pandas as pd

# To-Do
# 1. Get rows with specific values
# 2. Get rows with empty cells
# 3. analyze data

# get tabular data from external file
df2 = pd.read_csv('data.csv')

# perform some filteration on data on some cloumn
print(df2['customer_id'].max())
print(df2['customer_id'].min())
print(df2['customer_id'].any())

# Describe, will describe the dataform all columns for mean, median, mix, max etc
print(df2.describe())

# will print the first n rows
print(df2.head(7))

# datatype of each column
print(df2.dtypes)

print(df2.info())


# subset of dataframe
subset = df2[['order_id','product_name']]
print(subset)

print(" ")
print(" ")

# filter on the basis of values
print(df2[df2['rating'] > 4 ])

# use the series of boolean true, false to be used as argument
# it will only select rows which are true
bool_series = pd.Series([True, False, False, True, False, False, True])
print(df2[bool_series])

# isin() method
print("")
print("")
print(df2[df2['rating'].isin([3])])

# or operator
print(df2[(df2['rating'] == 4) | (df2['rating'] == 3) ])

print(" ")
# when the value is not know
print(df2[df2['rating'].notna()])

print(" ")
#print(df2[df2['rating']])

# usage of loc and iloc
print(df2.loc[df2['rating'] > 3, ['order_id', 'customer_id']])
print(df2.iloc[[2,1,4,5],[3,4]])

# print the info
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

# print(df['Sex'])
#
# print(df.index[0])
# print(df.columns[1])


# adding a new columm

df2['projected_value'] = df2['rating']*2

print(df2.head())


