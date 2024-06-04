# 定义
fruit = ['apple', 'orange', 'banana']
print(fruit) # ['apple', 'orange', 'banana']
print(type(fruit)) # <class 'list'>
# 获取长度
print(len(fruit)) # 3
# 获取元素
print(fruit[1]) # orange
print(fruit[-1]) # banana
# 修改元素
fruit[1] = 'black barry'
print(fruit) # ['apple', 'black barry', 'banana']
# 增加元素
fruit.append('greap')
print(fruit) # ['apple', 'black barry', 'banana', 'greap']
# 元素类型可以不同
fruit.append(100)
print(fruit) # ['apple', 'black barry', 'banana', 'greap', 100]
# 从末尾删除元素
fruit.pop()
print(fruit) # ['apple', 'black barry', 'banana', 'greap']
# 删除索引位置的元素
a = fruit.pop(2)
print(a) # banana
print(fruit) # ['apple', 'black barry', 'greap']
# 插入元素
fruit.insert(1, 'orange')
print(fruit) # ['apple', 'orange', 'black barry', 'greap']
# 根据索引删除
del fruit[0]
print(fruit) # ['orange', 'black barry', 'greap']
# 根据索引删除
fruit.pop(1)
print(fruit) # ['orange', 'greap']
# 根据值删除
fruit.remove('greap')
print(fruit) # ['orange', 'black barry']
# 清空
fruit.clear()
print(fruit) # []
fruit = ['apple', 'orange', 'banana']
# 遍历
for f in fruit:
    print(f) # orange black barry
# 列表生成式
for r in range(1, 10):
    print(r ** 2) # 1 4 9 16 25 36 49 64 81
vagetable = ['potato', 'tomato']
fruit.extend(vagetable)
print("---")
print(fruit) # ['apple', 'orange', 'banana', 'potato', 'tomato']
# 合并列表
food = fruit + vagetable
print(food) # ['apple', 'orange', 'banana', 'potato', 'tomato']
# 复制列表
food_copy = food[:]
print(food_copy) # ['apple', 'orange', 'banana', 'potato', 'tomato']
# 列表排序
food.sort()
print(food) # ['apple', 'banana', 'orange', 'potato', 'tomato']
# 列表倒序
food.sort(reverse=True)
print(food) # ['tomato', 'potato', 'orange', 'banana', 'apple']
# 列表反转
food.reverse()
print(food) # ['apple', 'banana', 'orange', 'potato', 'tomato']
# 列表切片
print(food[1:3]) # ['banana', 'orange']
print(food[:3]) # ['apple', 'banana', 'orange']
print(food[1:]) # ['banana', 'orange', 'potato', 'tomato']
print(food[-2:]) # ['potato', 'tomato']
# 列表反向切片复制
food = food[::-1]
print(food) # ['tomato', 'potato', 'orange', 'banana', 'apple']




