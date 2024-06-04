# 定义
tuple = ('a', True, 1, 1.1, [1, 2, 3])
print(tuple) # ('a', True, 1, 1.1, [1, 2, 3])
print(type(tuple)) # <class 'tuple'>
# 获取元素
print(tuple[0]) # a

# 元组的元素不可修改
# tuple[0] = 'b' # TypeError: 'tuple' object does not support item assignment
# 元组的元素可以是列表，列表的元素是可以修改的
tuple[4][0] = 2
print(tuple) # ('a', True, 1, 1.1, [2, 2, 3])

# 遍历
for t in tuple:
    print(t) # a True 1 1.1 [2, 2, 3]

# 元组的方法
# 获取元素的索引
print(tuple.index(1)) # 2
# 获取元素的个数
print(tuple.count(1)) # 1
# 获取元组的长度
print(len(tuple)) # 5
# 元组的合并
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3) # (1, 2, 3, 4, 5, 6)
# 元组的复制
tuple4 = tuple3[:]
print(tuple4) # (1, 2, 3, 4, 5, 6)
# 元组的排序
tuple5 = (3, 2, 1)
tuple6 = sorted(tuple5)
print(tuple6) # [1, 2, 3]
# 元组的反转
tuple7 = (1, 2, 3)
tuple8 = tuple7[::-1]
print(tuple8) # (3, 2, 1)
# 元组的清空
tuple9 = (1, 2, 3)
tuple9 = ()
print(tuple9) # ()
# 元组的删除
tuple10 = (1, 2, 3)
del tuple10
# print(tuple10) # NameError: name 'tuple10' is not defined
# 元组的切片
tuple11 = (1, 2, 3, 4, 5)
print(tuple11[1:3]) # (2, 3)
print(tuple11[1:]) # (2, 3, 4, 5)
print(tuple11[:3]) # (1, 2, 3)
print(tuple11[-1]) # 5
print(tuple11[-3:-1]) # (3, 4)
# 元组的拷贝
tuple12 = (1, 2, 3)
tuple13 = tuple12
print(tuple13) # (1, 2, 3)
# 元组的比较
tuple14 = (1, 2, 3)
tuple15 = (1, 2, 3)
print(tuple14 == tuple15) # True
print(tuple14 != tuple15) # False
print(tuple14 > tuple15) # False

# 元组的解包
a, b, c = (1, 2, 3)
print(a) # 1

# 将元组转换成列表
list = list(tuple)
print(list) # ['a', True, 1, 1.1, [2, 2, 3]]

# 将列表转换成元组
tuple = tuple(list)
print(tuple) # ('a', True, 1, 1.1, [2, 2, 3])



