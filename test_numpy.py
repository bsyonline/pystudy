# conda install numpy
import numpy as np

r = np.random.randint(1, 10)
print(r)

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
arr1 = np.array(l1)
arr2 = np.array(l2)

print(l1)
print(l2)
print(l1 + l2)

print(arr1)
print(arr2)
print(arr1 + arr2)

print(arr1 * 10)

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_data = np.array(data)
print(np_data)
print(type(np_data))

print(np.zeros((4, 4)))
print(np.ones((3, 3)))
print(np.empty((2,2)))

np_list = np.arange(10)
print(np_list)
print(np_list[3])
np_list[5:] = 10
print(np_list)

np_copy = np_list.copy()
np_copy[5:] = 20
print(np_list)
print(np_copy)