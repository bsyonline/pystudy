class Car():
    def __init__(self, category):
        self.category = category

    def toString(self):
        print("this is " + self.category + " car")


class ElectricCar(Car):
    def __init__(self, category):
        super().__init__(category)

    def toString(self):
        print("this is " + self.category + " car")
