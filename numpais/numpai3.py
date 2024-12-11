import numpy as np

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print("min for rows ",a.min(axis=1))
print("min overall", a.min())

print("max for rows ",a.max(axis=1))
print("max overall", a.max())

print("sum for rows ",a.sum(axis=1))
print("sum overall", a.sum())

# unique
array1 = np.array([1,2,3,4,5,5,6,8,9,9,10,10,11,12])
unique_arr = np.unique(array1)
print(unique_arr)

# just return the indexes
indexes = np.unique(array1, return_index=True)
print(indexes)

# count occurrences
unique_occurences = np.unique(array1, return_counts=True)
print(unique_occurences)
