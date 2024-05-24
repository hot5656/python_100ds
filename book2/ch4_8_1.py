# 求某一點至一條線垂直線
# y = 0.5x - 0.5
# point (2,3)
# y = -2x + 7

from sympy import Symbol, solve
x = Symbol("x")
y = Symbol("y")
eq1 = 0.5*x - 0.5 - y
eq2 = -2*x + 7 - y
ans = solve((eq1, eq2))
print(ans)

import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

line_x = range(-5,6)
line_y = [0.5*x_no - 0.5 for x_no in line_x]
plt.plot(line_x, line_y)

line2_x = range(-5,6)
line2_y = [-2*x_no + 7 for x_no in line2_x ]
plt.plot(line2_x, line2_y)

# point (2,3)
point_x = 2
point_y = 3
plt.plot(point_x, point_y, "-o")
plt.text(point_x-0.25, point_y+0.5, f"({point_x}, {point_y})")

# point connection
plt.plot(ans[x], ans[y], "-o")
plt.text(ans[x]-0.25, ans[y]+0.5, f"({int(ans[x])}, {int(ans[y])})")

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
# x, y軸距長度一致
plt.axis('equal')

plt.show()
# {x: 3.00000000000000, y: 1.00000000000000}