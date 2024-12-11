import pandas as pd

data = pd.read_csv('air_quality_long.csv')

# filter on the basis of some column and its some value like
# those rows where parameter value is pm25, it also gets only one column e.g. country
df2 = data[data['parameter'] == 'pm25']['country']
rows = df2.shape

print(df2.head())

# get the rows and columns of datafarm
rows0, cols0 = data.shape
print(rows0, cols0)

# concate the tables
# 1. create two tables with different rows of the data e.g. get on the basis of parameter value
# 2. create two tables with different column of the data e.g. different columns
print("original table(rows, cols)", data.shape)
# 1 horizontally, get all the rows in the table where values for parameter is pm25
table1 = data[data['parameter'] == 'pm25']

# get all the rows in the table where value for parameter is no2
table2 = data[data['parameter'] == 'no2']

#print the rows, column
print("Table 1", table1.shape)
print("Table 2", table2.shape)

combined_table = pd.concat([table1, table2], axis=0)
print("combined table", combined_table.shape)

# scenarios # 2
table3 = data[data['parameter'] == 'pm25'][['city','country','parameter']]
# get all the rows in the table where value for parameter is no2
table4 = data[data['parameter'] == 'no2'][['date.utc','location','value','unit']]

vertical_combined_table = pd.concat([table3,table4], axis=1)
print("vertical_combined ", vertical_combined_table.shape)

# merge two tables on 'left join' when common column name exits
air_quality = pd.read_csv("air_quality_long.csv")
stations_coord = pd.read_csv("air_quality_stations.csv")
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
print(air_quality.head())

# merge two tables on 'left join', when no common name column exits
air_quality = pd.read_csv("air_quality_long.csv")
stations_coord = pd.read_csv("air_quality_parameters.csv")

air_quality = pd.merge(air_quality, stations_coord, how="left", left_on="parameter",
right_on='id')
print(air_quality.head())
