# 从xx模块导入xx类
from car import Car, ElectricCar

c = Car('benz')
c.toString()

e = ElectricCar('tesla')
e.toString()

# 导入整个模块
import bmw

b = bmw.BMW('bmw 7')
b.toString()
