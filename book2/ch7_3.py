# 一元二次方程式繪圖並算極值
# y = 3x**2 - 12x + 10 繪圖,標示兩個根,標極值
# y = -3x**2 + 12x - 9 繪圖,標示兩個根,標極值
# y = x**2 +  x + 1 (無根)
# 根的意義為 y 值為 0
from sympy import *

x = Symbol("x")
# y = 3x**2 - 12x + 10
f = 3*x**2 -12*x + 10
# y = -3x**2 + 12x - 9
# f = -3*x**2 + 12*x - 9
roots = solve(f)
# print(roots)

# y = 3x**2 - 12x + 10
def f(x) :
    return 3*x**2 -12*x + 10
def g(x) :
    return -f(x)

# y = -3x**2 + 12x - 9
def f2(x) :
    return -3*x**2 +12*x - 9

def g2(x) :
    return -f2(x)

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

# y = 3x**2 - 12x + 10
line_x =  np.linspace(0, 4, 100)
# line_y = [3*x_no**2 - 12*x_no + 10 for x_no in line_x]
# 與前面算式相等
line_y = 3*line_x**2 - 12*line_x + 10
# y = 3x**2 + 12x - 9
# line_x =  np.linspace(0, 4, 100)
# line_y = [-3*x_no**2 + 12*x_no - 9 for x_no in line_x]
# 無根
# line_x =  np.linspace(-4, 4, 100)
# line_y = [x_no**2 +  x_no + 1 for x_no in line_x]
plt.plot(line_x, line_y)

# 標示根
for root in roots:
    x_value = root.evalf()
    # y = 3x**2 - 12x + 10
    y_value = f(x_value)
    # y = -3x**2 + 12x - 9
    # y_value = f2(x_value)
    plt.plot(x_value, y_value, "-o")
    plt.text(x_value - 0.35, y_value + 0.4, f"({x_value:.2f},{y_value:.2f})")

# 標示極值
# y = 3x**2 - 12x + 10
peak = minimize_scalar(f)
# y = -3x**2 + 12x - 9
# peak = minimize_scalar(f2)
if not(np.isinf(peak.fun)):
    # 有最小值
    limit_y = peak.fun
else:
    # y = 3x**2 - 12x + 10
    peak = minimize_scalar(g)
    # y = -3x**2 + 12x - 9
    # peak = minimize_scalar(g2)
    if not(np.isinf(peak.fun)):
        # 有最大值
        limit_y = -peak.fun
if not(np.isinf(peak.fun)):
    plt.plot(peak.x, limit_y, "-o")
    plt.text(peak.x - 0.35, limit_y + 0.4, f"({peak.x:.2f},{limit_y:.2f})")

plt.show()