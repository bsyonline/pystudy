from car import Car


class BMW(Car):
    def __init__(self, category):
        super().__init__(category)

    def toString(self):
        print("this is BMW car")
