numbers = [3, 5, 8, 13]
print(numbers[1])
import numpy as np

arr = np.array([3, 5, 8, 13])
print(arr[0])

import numpy as np

scores = np.array([
    [88, 92, 79],
    [95, 85, 91],
    [76, 80, 84]
])

print(scores.shape)

numbers = np.array(
    [4, 7, 9, 12, 15]
)

print(numbers[0])
print(numbers[1])
print(numbers[0:3])
numbers=numbers*5+2
print(numbers)

munbers = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(munbers[0,1])
print(munbers[1])
print(munbers[:,2])
print(munbers.sum(axis=0))
print(munbers.sum(axis=1))
print(munbers.sum())
