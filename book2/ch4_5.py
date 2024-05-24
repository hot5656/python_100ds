# 雞兔同籠
# x + y = 35
# 2x + 4y = 100
from sympy import Symbol, solve
x = Symbol("x")
y = Symbol("y")
eq1 = x + y - 35
eq2 = 2*x + 4*y -100
ans = solve((eq1, eq2))
print(ans)
print(f"雞={ans[x]}")
print(f"兔={ans[y]}")


import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

x_p = range(0,101)
y1_p = [ 35 - x_no for x_no in x_p]
y2_p = [ (100 - 2*x_no)/4 for x_no in x_p]
plt.plot(x_p, y1_p)
plt.plot(x_p, y2_p)

plt.plot(ans[x], ans[y], "-o")
plt.text(ans[x], ans[y]+5, f"({ans[x]}, {ans[y]})")

plt.xlabel('雞')
plt.ylabel('兔')
plt.grid()

plt.show()

# {x: 20, y: 15}
# 雞=20
# 兔=15
