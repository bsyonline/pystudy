# 定义class
class Employee():
    # 默认方法，python会自动执行
    def __init__(self, id, name, age):
        print("__init__")
        self.id = id
        self.name = name
        self.age = age
        self.type = "employee"
        # 私有变量
        self.__private_name = name

    def get_private_name(self):
        return self.__private_name

    def work(self):
        print("%s %s work" % (self.type, self.name))

    def to_string(self):
        return ("employee:{id=" + str(self.id) + ", name=" + self.name + ", age="
                + str(self.age) + ", type=" + self.type + ", private_name=" + self.__private_name + "}")


# 实例化
print("before inst")
e = Employee(1, "zhangsan", 18)
print("after inst")
print(e)
print("employee id:" + str(e.id))
print("employee name:" + e.name)
print("employee age:" + str(e.age))
print("employee type:" + e.type)
# 外部不能访问私有变量
# print(e.__private_name)
print("employee private name:" + e.get_private_name())
e.work()
print(e.to_string())
print("---")
e1 = Employee(2, "lisi", 20)
print(e1)
print("employee id:" + str(e1.id))
print("employee name:" + e1.name)
print("employee age:" + str(e1.age))
print("employee type:" + e1.type)
print("employee private name:" + e.get_private_name())
print(e1.to_string())
# 修改属性的值
e1.age = 22
print(e1.to_string())
print("---")

class Manager(Employee):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.type = "manager"

    # 方法重写
    def work(self):
        print("manager work")


# class 继承
m = Manager(3, "wangwu", 30)
m.work()
print("employee id:" + str(m.id))
print("employee name:" + m.name)
print("employee age:" + str(m.age))
print("employee type:" + m.type)
print(m.to_string())