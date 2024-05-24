# 行銷問題分析
# 每月行銷次數 增加業績
#     1         10萬
#     2         18萬
#     3         19萬
# y = ax**2 + b*x + c
# a + b + c = 10
# 4a + 2b + c = 18
# 9a + 3b + c = 18

from sympy import Symbol, symbols, solve
a, b, c = symbols(("a", "b", "c"))
eq1 = a + b + c - 10
eq2 = 4*a + 2*b + c - 18
eq3 = 9*a + 3*b + c - 19
ans = solve((eq1, eq2, eq3))
print(ans)
# {a: -7/2, b: 37/2, c: -5}

# x 要放在最前面
def f(x, a, b, c) :
    return (a*x**2 + b*x + c)
def g(x, a, b, c) :
    return -f(x, a, b, c)

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(0, 5, 50)
y = ans[a]*x**2 + ans[b]*x + ans[c]
plt.plot(x,y)

# 算最大值
print(ans[a].evalf(), ans[b].evalf(), ans[c].evalf())
# args 不含 x, 要轉成 float 才不會有問題
args = (float(ans[a].evalf()), float(ans[b].evalf()), float(ans[c].evalf()))
peak = minimize_scalar(g, args=args)
limit_y = -peak.fun
print(f"max ({peak.x},{limit_y})")
plt.plot(peak.x,limit_y, "-o")
plt.text(peak.x-0.3,limit_y-2, f"({peak.x:.1f},{limit_y:.1f})")
# -3.50000000000000 18.5000000000000 -5.00000000000000
# max (2.6428571428571432,19.446428571428577)

# 算業績15萬的交叉點
# 15 = -3.5**2 + 18.5*x - 5
ask_y = 15
x2 = Symbol("x2")
eq = -3.5*x2**2 + 18.5*x2 - 20
ans2 = solve(eq)
print(ans2)
for x_value in ans2:
    plt.plot(x_value,ask_y, "-o", color="green")
    plt.text(x_value+0.1,ask_y, f"({x_value:.1f},{ask_y:.1f})")
plt.grid()
plt.show()
