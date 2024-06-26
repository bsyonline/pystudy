# conda install numpy
import numpy as np


# 创建数组
# 从列表创建1维数组
arr1 = np.array([1, 2, 3])
print(arr1)
# 从列表创建2维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
# 从1到3，不包括3
arr3 = np.arange(1, 3)
print(arr3)
# 从1到5，步长为2
arr4 = np.arange(1, 5, 2)
print(arr4)
# 从1到3，分成3份
arr5 = np.linspace(1, 3, 3)
print(arr5)
# 从1到3，分成3份，取幂
arr6 = np.logspace(1, 3, 3)
print(arr6)
# 从string创建
arr7 = np.fromstring("1, 2, 3", sep=",")
print(arr7)
# 随机生成3个数
arr8 = np.random.randint(1, 10, 3)
print(arr8)
# 创建全0数组
arr9 = np.zeros(3)
print(arr9)
# 3x3全0数组
arr10 = np.zeros((3, 3))
print(arr10)
# 创建全1数组
arr11 = np.ones(3)
print(arr11)
# 3x3全1数组
arr12 = np.ones((3, 3))
print(arr12)
# 创建全空数组
arr13 = np.empty(3)
print(arr13)
# 3x3全空数组
arr14 = np.empty((3, 3))
print(arr14)



# print("\n--numpy随机数--")
# r = np.random.randint(1, 10)
# print(r)
#
# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9, 10]
# # 深拷贝
# arr1 = np.array(l1)
# # 浅拷贝
# arr2 = np.asarray(l2)
# print("\n--普通数组相加--")
# print(l1)
# print(l2)
# # 普通array相加是数组拼接
# print(l1 + l2)
#
# print("\n--nparray数组相加--")
# print(arr1)
# # 数组的维度
# print(arr1.ndim)
# # 数组的形状
# print(arr2.shape)
# # nparray相加是按为相加
# print(arr1 + arr2)
#
# print("\n--nparray数组相乘--")
# # nparray相乘是按为相乘
# print(arr1 * 10)
#
# print("\n--nparray构造2维数组--")
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# np_data = np.array(data)
# print(np_data)
# print(type(np_data))
# # 数组中元素类型
# print(np_data.dtype)
# # 改变数组元素的类型，新数组
# print(np_data.astype('str'))
# print(np_data.shape)
# print(np_data.size)
#
# print("\n--reshape--")
# reshape_data = np_data.reshape((9, 1))
# print(reshape_data)
# print(reshape_data.shape)
#
# print("\n--填充零--")
# print(np.zeros((4, 4)))
#
# print("\n--填充1--")
# print(np.ones((3, 3)))
#
# print("\n--置空--")
# print(np.empty((2, 2)))
#
# print("\n--声明列表--")
# np_list = np.arange(10)
# print(np_list)
# print(np_list[3])
# # 从5到10（包括5不包括10）
# print(np.arange(5, 10))
# # 从1到10（不包括10），步长=2
# print(np.arange(1, 10, 2))
#
# print("\n--分片--")
# np_list[5:] = 10
# print(np_list)
#
# print("\n--拷贝--")
# np_copy = np_list.copy()
# np_copy[5:] = 20
# print(np_list)
# print(np_copy)
#
# print("\n--创建等差数列--")
# # 从2到20，元素为3的等差数列
# print(np.linspace(start=2, stop=20, num=3))
#
# np_arr = np.asarray([[4, 7, 5],
#                      [4, 2, 5],
#                      [7, 2, 4],
#                      [1, 2, 4]])
# print(np_arr.sum(axis=1) / 3)
# print(np.average(np_arr, axis=1))
#
# scores = np.random.rand(256, 256, 2)
# scores[:, :, 1] = 1 - scores[:, :, 0]
# print(scores)
# print(np.argmax(scores, axis=2))
