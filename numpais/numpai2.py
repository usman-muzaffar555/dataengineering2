import numpy as np
# sum array
a = np.array([1,2,3,4,5,6,7])
sum_of_array=a.sum()
print(sum_of_array)

b = np.array([[1,2,3,4],
              [10,11,12,13],
              [20,21,22,23]])

c = np.array([[50,51,52,53],
              [60,61,62,63],
              [70,71,72,73]])
d=b.sum(axis=0)
e=c.sum(axis=1)

print(d)
print(e)

#broadcating , any arithmetic operation can be performed
# both one dimensional or single value
race_kilometer = np.array([1,3,4,5])
race_mile = race_kilometer * 1.6
print(race_mile)
race2 = np.array([100,100,100,100])
race3 = race_kilometer * race2
print(race3)

# one dimensional and two dimensional
race2 = np.array([[100,100,100,100], [20,20,20,20]])
race3 = np.array([[100,100,100,100]])

race4 = race2 * race3
print(race4)

#  two dimensional
race5 = np.array([[100,100,100,100], [20,20,20,20]])
race6 = np.array([[100,100,100,100],[100,100,100,100]])

race7 = race5 * race6
print(race7)
