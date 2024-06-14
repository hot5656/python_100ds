# 網購迴歸曲線繪製
# 購物網站 24 hour vs 購物人數
import matplotlib.pyplot as plt
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,
     12,13,14,15,16,17,19,21,22,23,24]
y = [100, 88, 75, 60, 50, 55, 55, 56, 58, 58, 61,
      63, 68, 71, 71, 75, 76, 88, 93, 97, 97, 100]

# 建立一次函數迴歸模型係數
# 建立一次函數迴歸方程式
coef1 = np.polyfit(x, y, 1)
model1 = np.poly1d(coef1)

# 建立二次函數迴歸模型係數
# 建立二次函數迴歸方程式
coef2 = np.polyfit(x, y, 2)
model2 = np.poly1d(coef2)

# 建立三次函數迴歸模型係數
# 建立三次函數迴歸方程式
coef3 = np.polyfit(x, y, 3)
model3 = np.poly1d(coef3)

print(model1)
print(model2)
print(model3)

plt.plot(x, model1(x) , color='blue', label="1次函")
plt.plot(x, model2(x) , color='green', label="2次函")
plt.plot(x, model3(x) , color='red', label="3次函")

plt.scatter(x, y )
plt.title("網路購物調查")
plt.xlabel("時間")
plt.ylabel("購物人數")
plt.legend()
plt.show()

# 1.207 x + 59.03
#         2
# 0.2591 x - 5.279 x + 87.1
#           3         2
# -0.02715 x + 1.275 x - 15.51 x + 110.2

