class Person:
    __slots__ = ('_name', '_age')

    def __init__(self, name, age=None):
        self._name = name
        if age is not None:
            self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


def main():
    s = Person("zhangsan")
    print(s.name)
    s.age = 18
    print(s.age)
    # s.gender = 'male'
    # print(s.gender)


if __name__ == '__main__':
    main()
