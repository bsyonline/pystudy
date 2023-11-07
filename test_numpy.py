import numpy as np

print("\n--numpy随机数--")
r = np.random.randint(1, 10)
print(r)

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
# 深拷贝
arr1 = np.array(l1)
# 浅拷贝
arr2 = np.asarray(l2)
print("\n--普通数组相加--")
print(l1)
print(l2)
# 普通array相加是数组拼接
print(l1 + l2)

print("\n--nparray数组相加--")
print(arr1)
# 数组的维度
print(arr1.ndim)
print(arr2.ndim)
# nparray相加是按为相加
print(arr1 + arr2)

print("\n--nparray数组相乘--")
# nparray相乘是按为相乘
print(arr1 * 10)

print("\n--nparray构造2维数组--")
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_data = np.array(data)
print(np_data)
print(type(np_data))

print("\n--填充零--")
print(np.zeros((4, 4)))

print("\n--填充1--")
print(np.ones((3, 3)))

print("\n--置空--")
print(np.empty((2,2)))

print("\n--声明列表--")
np_list = np.arange(10)
print(np_list)
print(np_list[3])

print("\n--分片--")
np_list[5:] = 10
print(np_list)

print("\n--拷贝--")
np_copy = np_list.copy()
np_copy[5:] = 20
print(np_list)
print(np_copy)