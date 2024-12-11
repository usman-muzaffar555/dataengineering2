import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print("a ", a)
# save to an external file
np.save('test_a',a)
# load from external file
b = np.load('test_a.npy')
print("b ", b)


# save in text and csv file format
np.savetxt('a_file.csv', a)
np.savetxt('a_file.txt', a)

