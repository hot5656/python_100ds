# y = 0.03x - 18
# 餐聽 x:消費人數, 單位萬
# show x = 0 ~ 1000
import matplotlib.pyplot as plt
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(0, 1000, 101)
y = 0.03 * x - 18
# x 顯示範圍 , y 顯示範圍
plt.axis([0 , 1000, -20, 15])
plt.plot(x,y)
plt.title('餐廳利潤對照表')
plt.xlabel('顧客人數')
plt.ylabel('利潤/萬元')
plt.grid()

plt.show()

