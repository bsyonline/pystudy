class Teacher:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self.__gender = gender

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def gender(self):
        return self.__gender

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age


def main():
    s = Teacher("zhangsan", 18, 'male')
    print(s.name)
    print(s.gender)
    print(s.age)
    s.age = 21
    print(s.age)


if __name__ == '__main__':
    main()
