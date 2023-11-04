def f1():
    print("this is a function")


f1()


# 带参数的函数
def f2(name):
    print("hello, " + name)


f2("zhangsan")


def f3(name, age):
    print(name + " is " + str(age) + " years old.")


f3("lisi", 30)  # 传值要按顺序
f3(name="tom", age=21)
f3(age=21, name="kate")  # 指定参数名字，可以不按照形参顺序


# 参数有默认值
def f4(name, gender='male'):
    print(name + "'gender is " + gender)


f4('jack')  # 定义了默认值可以不传
f4('lily', 'female')


# 有返回值的函数
def f5(a, b):
    return a + b


r = f5(1, 2)
print(r)
