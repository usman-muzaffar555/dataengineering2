import pandas as pd

# get the data
air_quality = pd.read_csv("air_quality_long.csv")
# text to date object
air_quality['date-obj'] = pd.to_datetime(air_quality['date.utc'])

print("min", air_quality['date-obj'].min())
print("min", air_quality['date-obj'].max())

print(air_quality.head())

# time difference
print(air_quality['date-obj'].max() - air_quality['date-obj'].min())

# different days of a date
print(air_quality['date-obj'].
      dt.month.head())
print(air_quality['date-obj'].
      dt.year.head())


# get the location-wise count for each day of the week
print("weekday ", air_quality.groupby(
    [air_quality['date-obj'].dt.weekday, "location"]).count())


# get the count for one location for each day of the week
air_quality = pd.read_csv("air_quality_long.csv")
air_quality['date-obj'] = pd.to_datetime(air_quality['date.utc'])

print("weekday 0 ",
    (air_quality.loc[(air_quality["location"]=='BETR801') &
                    (air_quality["date-obj"].dt.weekday == 0)].groupby('location')).count())
print("weekday 1",
    (air_quality.loc[(air_quality["location"]=='BETR801') &
                    (air_quality["date-obj"].dt.weekday == 1)].groupby('location')).count())
print("weekday 2",
    (air_quality.loc[(air_quality["location"]=='BETR801') &
                    (air_quality["date-obj"].dt.weekday == 2)].groupby('location')).count())
print("weekday 3",
    (air_quality.loc[(air_quality["location"]=='BETR801') &
                    (air_quality["date-obj"].dt.weekday == 3)].groupby('location')).count())
print("weekday 4",
    (air_quality.loc[(air_quality["location"]=='BETR801') &
                    (air_quality["date-obj"].dt.weekday == 4)].groupby('location')).count())
print("weekday 5",
    (air_quality.loc[(air_quality["location"]=='BETR801') &
                    (air_quality["date-obj"].dt.weekday == 5)].groupby('location')).count())
print("weekday 6",
    (air_quality.loc[(air_quality["location"]=='BETR801') &
                    (air_quality["date-obj"].dt.weekday == 6)].groupby('location')).count())