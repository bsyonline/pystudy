class Student:
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 默认方法，python会自动执行
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age
        self.__gender = gender


def main():
    s = Student("zhangsan", 18, 'male')
    print(s.name)
    print(s._age)
    # print(s.__gender) # AttributeError: 'student' object has no attribute '__gender'
    print(s._Student__gender)


if __name__ == '__main__':
    main()
