# 定义class
class Employee():
    # 默认方法，python会自动执行
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.type = "employee"

    def work(self):
        print("employee work")

    def toString(self):
        return "employee:{id=" + str(self.id) + ", name=" + self.name + ", age=" + str(
            self.age) + ", type=" + self.type + "}"


# 实例化
e = Employee(1, "zhangsan", 18)
print(e)
print("employee id:" + str(e.id))
print("employee name:" + e.name)
print("employee age:" + str(e.age))
print("employee age:" + e.type)
e.work()
print("employee type:" + e.toString())

e1 = Employee(2, "lisi", 20)
print("employee id:" + str(e1.id))
print("employee name:" + e1.name)
print("employee age:" + str(e1.age))
print("employee type:" + e1.toString())

# 修改属性的值
e1.age = 22
print(e1.toString())


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
print(m.toString())
