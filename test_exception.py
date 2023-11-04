a = input("first number: ")
b = input("second number: ")
try:
    print(int(a)/int(b))
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("必须输入整数")

try:
    with open("aaa") as f:
        f.readlines()
except FileNotFoundError:
    print("file not exist")

# 忽略异常
try:
    i = 1/0
except ZeroDivisionError:
    pass