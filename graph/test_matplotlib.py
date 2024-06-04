# 生成 y= x^2 函数图像
import matplotlib.pyplot as plot
import numpy as np

x = np.arange(-50, 50, 2)
y = x ** 2

plot.plot(x, y, color='blue')
plot.legend()
plot.show()
