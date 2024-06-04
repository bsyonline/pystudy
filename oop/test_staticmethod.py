class Person:

    def __init__(self, name, age):
        self._name = name
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

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 120


def main():
    age = -1
    if Person.is_age_valid(age):
        s = Person("zhangsan", age)
        print(s.name)
        s.age = 18
        print(s.age)
    else:
        print("Valid age")


if __name__ == '__main__':
    main()
