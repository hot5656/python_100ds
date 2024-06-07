# 角度繪圓
import matplotlib.pyplot as plt
# import numpy as np
import math

degrees = [x*15 for x in range(0,25)]
x = [math.cos(math.radians(d)) for d in degrees]
y = [math.sin(math.radians(d)) for d in degrees]

plt.scatter(x, y)
plt.plot(x,y)
plt.axis("equal")
plt.grid()
plt.show()