import numpy as np

a=np.arange(10)
print(a)

b=np.arange(2, 10, dtype=float)
print(b)

c=np.arange(2, 3, 0.1)
print(c)

# np.eye defines 2d array with value 1 at same row/col index and 0 otherwise
td=np.eye(3)
print(td)

td2=np.eye(3,5)
print(td2)

# ndarray.ndim, ndarray.size, ndarray.shape
print(td2.ndim)
print(td2.size)
print(td2.shape)

# reshape
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("arr ", arr)

reshaped = arr.reshape(5,3)
print(reshaped)
print(reshaped.ndim)
print(reshaped[0][0])

# how to get the row, col size separately ???

# conditional selection of elements
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
five_up = (a >= 5)
print(five_up)
five_above = a[five_up]
print(five_above)

three_divisive = (a%3==0)
array3 = a[three_divisive]
print(array3)

# slice the array and make new array
bread = np.array([[100,101,102,103,104,105],
                  [200,201,202,203,204,205],
                  [300,301,302,303,304,305]])

slice = bread[0:3,2:3] # row index(e.g. from 0 rows to 2), col index(e.g. col 2 to 2)
print(slice[1][0])

bread2 = np.array([1,2,3,4,5,5,6,8,9,9,10,10,11,12])
slice2 = bread2[5:10]
print(slice2)
#
tdim = np.array([[1,2,3,4,5],
                [10,11,12,13,14],
                [20,21,22,23,24]])
print(tdim[(1,2),1])
print(tdim[(1,2),:])


# deep copy and normal assignment
array1 = np.array([1,2,3,4,5,5,6,8,9,9,10,10,11,12])
array2 = array1
array_d_copy = array1.copy()

# make some change in original array
array1[11]=11

print("array1", array1)
print("array2", array2)
print("array deep copy", array_d_copy)