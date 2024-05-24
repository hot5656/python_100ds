# 業務目標計算
# x + y = 100(天)
# 2x + 4y = 350(萬)
from sympy import Symbol, solve
x = Symbol("x")
y = Symbol("y")
eq1 = x + y - 100
eq2 = 2*x + 4*y - 350
ans = solve((eq1, eq2))
print(ans)
print(f"菜鳥業務={ans[x]}")
print(f"資深業務={ans[y]}")

import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

line_x = range(0,101)
line1_y = [ 100 - x_no for x_no in line_x]
line2_y = [ (350 - 2*x_no)/4 for x_no in line_x]
plt.plot(line_x, line1_y)
plt.plot(line_x, line2_y)

plt.plot(ans[x], ans[y], "-o")
plt.text(ans[x], ans[y]+5, f"({ans[x]}, {ans[y]})")

plt.xlabel('菜鳥業務')
plt.ylabel('資深業務')
plt.grid()

plt.show()
