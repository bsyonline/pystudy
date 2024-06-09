from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def work(self):
        pass


class Sales(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.type = "sales"

    def work(self):
        print("sales work")


class RD(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.type = "RD"

    def work(self):
        print("RD work")


class Car(object):
    def work(self):
        print("car run")


def main():
    e = Sales(1, "zhangsan")
    print(e.id)
    print(e.name)
    e.work()
    m = RD(2, "lisi")
    print(m.id)
    print(m.name)
    print(m.type)
    m.work()
    c = Car()
    c.work()


if __name__ == '__main__':
    main()
