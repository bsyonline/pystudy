class Animal:
    def run(self):
        print("animal run")


class Dog(Animal):
    pass


class Cat(Animal):
    def run(self):
        print("cat run")


class Car(object):
    def run(self):
        print("car run")


def run(animal):
    animal.run()


animal = Animal()
dog = Dog()
cat = Cat()
car = Car()
run(animal)
run(dog)
run(cat)
# car有run方法就可以调用，不需要继承Animal
run(car)
