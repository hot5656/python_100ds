# 垂直相交線
# y = x
# y = -x + 2
from sympy import Symbol, solve
x = Symbol("x")
y = Symbol("y")
eq1 = x - y
eq2 = -x + 2 - y
ans = solve((eq1, eq2))
print(ans)


import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

line_x = range(-5,5)
line1_y = [  x_no for x_no in line_x]
line2_y = [ -x_no + 2 for x_no in line_x]
plt.plot(line_x, line1_y)
plt.plot(line_x, line2_y)

plt.plot(ans[x], ans[y], "-o")
plt.text(ans[x]-0.25, ans[y]+0.5, f"({ans[x]}, {ans[y]})")

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()

plt.show()
# {x: 1, y: 1}