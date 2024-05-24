# 餐廳營利計算
# P(600,0)      600a  + b = 0
# P(1000,12)    1000a + b = 12 --> 1000a + b - 12 = 0
from sympy import Symbol, solve
a = Symbol("a")
b = Symbol("b")
# 定義公式要右邊為 0
eq1 = 600 * a + b
eq2 = 1000 * a + b - 12
ans = solve((eq1, eq2))
# print(ans)
print(f"a={ans[a]}")
print(f"b={ans[b]}")
# print(f"{type(ans[a])}")
# a=3/100
# b=-18
# y = 0.03x - 18

import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

points_x = [600, 1000]
points_y = [ px * ans[a] + ans[b] for px in points_x]
plt.plot(points_x, points_y, "-o")

x = range(0, 2500, 10)
y = [ans[a] * y - 18 for y in x]
# x 顯示範圍 0~1000, y 顯示範圍 -20~15
# plt.axis([0,1000, -20, 15])
plt.plot(x,y)
plt.title('餐廳營利對照圖', fontsize=20)
plt.xlabel('人數')
plt.ylabel('利潤/萬元')
plt.grid()

# 列出1500人 利潤
people1 = 1500
frofit1 = people1 * ans[a] + ans[b]
print(f"f({people1}) = {frofit1}")
plt.plot(people1, frofit1, "-o", color='red')
# show 文字
plt.text(people1-170, frofit1+5, f"({people1}, {frofit1})")

# 列出利潤 48 萬
frofit2 = 48
people2 = (frofit2 - ans[b]) / ans[a]
print(f"f({people2}) = {frofit2}")
plt.plot(people2, frofit2, "-o", color='red')
# show 文字
plt.text(people2-170, frofit2+5, f"({people2}, {frofit2})")

plt.show()

# a=3/100
# b=-18
# f(1500) = 27
# f(2200) = 48