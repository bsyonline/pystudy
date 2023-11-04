t = ("zhangsan", 20)
print(t)
print(type(t))
print(t[0])
print(t[1])

for e in t:
    print(e)

# t[1] = 21 元组的元素不能赋值
t = ("zhangsan", 21)  # 元组可以赋值

print(t)
