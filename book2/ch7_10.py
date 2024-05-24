# 求一元二次方程式,並繪圖
# 匯出 100, 200, 300 的點,及預估 400 的點
# 拜訪次數(1=100次) vs 業績(回收問卷)
# y = ax**2 + bx + c
# x = 1, y =500 --> 500 = a + b +c
# x = 2, y =1000 --> 1000 = 4a + 2b +c
# x = 3, y =2000 --> 2000 = 9a + 3b +c
from sympy import symbols, solve
import numpy as np
import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

def y_count(a, b, c, x):
    return (a*x**2 + b*x + c)

a, b, c = symbols(("a", "b", "c"))
eq1 = a + b + c - 500
eq2 = 4*a + 2*b + c - 1000
eq3 = 9*a + 3*b + c - 2000
ans = solve((eq1, eq2, eq3))
print(ans)
# {a: 250, b: -250, c: 500}

x = np.linspace(0, 5, 50)
y = ans[a]*x**2 + ans[b]*x + ans[c]
plt.plot(x,y)

for i in range(1,5):
    y_axis = y_count(ans[a], ans[b], ans[c], i)
    plt.plot(i, y_axis, "-o", color="green")
    plt.text(i - 0.6, y_axis + 200, f"({i},{y_axis})")

# 計算回收 3000 張問卷,拜訪次數
from sympy import Symbol, solve
count_value = 3000
z = Symbol("z")
eq = ans[a]*z**2 + ans[b]*z + ans[c] - count_value
ans_3000 = solve(eq)
print(ans_3000)
# [1/2 - sqrt(41)/2, 1/2 + sqrt(41)/2]
for ans_item in ans_3000:
    ans_value = ans_item.evalf()
    print(ans_value)
    if (ans_value > 0):
        plt.plot(ans_value, count_value, "-o", color="red")
        plt.text(ans_value - 0.8, count_value + 200, f"({ans_value:.2f},{count_value})")
# -2.70156211871642
# 3.70156211871642

plt.xlabel('拜訪次數(單位=100)')
plt.ylabel('業績')
plt.grid()
plt.show()
