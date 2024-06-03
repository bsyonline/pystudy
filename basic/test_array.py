# 定义
fruit = ['apple', 'orange', 'banana']
print(fruit)
print(type(fruit))

# 获取元素
print(fruit[1])

# 修改元素
fruit[1] = 'black barry'

# 增加元素
fruit.append('greap')

# 元素类型可以不同
fruit.append(100)
print(fruit)

# 从末尾删除元素
fruit.pop()
print(fruit)

# 删除索引位置的元素
a = fruit.pop(2)
print(a)
print(fruit)

del fruit[0]
print(fruit)

# 根据值删除
fruit.remove('greap')
print(fruit)

print("--")

# 遍历
for f in fruit:
    print(f)

for r in range(1, 10):
    print(r ** 2)