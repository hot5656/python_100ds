# 開發分析
# 商用軟體: 開發費用90萬,包裝介面設計50萬
# App軟體 : 開發費用150萬,包裝介面設計20萬
# 研發成本<=1200萬
# 包裝介面<=350萬
# 每個按鍵獲利50萬,計算最大獲利
# 90x + 150y <= 1200 --> y <= -0.6x + 8
# 50x + 20y  <= 350  --> y <= -2.5x + 17.5
# z = 50x + 50y
# (若獲利 600萬) 50x + 50y = 600 --> y = -x + 12
# (5, 5) --> 50*5 + 50*5 = 500 --> y = -x + 10

from sympy import Symbol, solve

# 求 line1 line2 交叉
x = Symbol("x")
y = Symbol("y")
eq1 = -0.6*x + 8  - y
eq2 = -2.5*x + 17.5 - y
ans = solve((eq1, eq2))
print(ans)

import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

line_x = range(0,15)
line1_y = [ -0.6*x_no + 8 for x_no in line_x ]
line2_y = [ -2.5*x_no + 17.5 for x_no in line_x ]
plt.plot(line_x, line1_y)
plt.plot(line_x, line2_y)

# add point connection
plt.plot(ans[x], ans[y], "-o")
plt.text(ans[x]-0.25, ans[y]+0.5, f"({int(ans[x])}, {int(ans[y])})")

line3_x = range(0,15)
# 獲利 600萬
# line3_y = [ -x_no + 12 for x_no in line3_x ]
# 獲利 500萬
line3_y = [ -x_no + 10 for x_no in line3_x ]
plt.plot(line3_x, line3_y, lw='2.0', color="green")

plt.xlabel('商用軟體')
plt.ylabel('App軟體')
# 表格顯示範圍 x:0~20,y:0~20
plt.axis([0, 20, 0, 20])
plt.grid()

plt.show()
# {x: 5.00000000000000, y: 5.00000000000000}