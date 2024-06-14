import matplotlib.pyplot as plt
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,
     12,13,14,15,16,17,19,21,22,23,24]
y = [100, 88, 75, 60, 50, 55, 55, 56, 58, 58, 61,
      63, 68, 71, 71, 75, 76, 88, 93, 97, 97, 100]

coef = np.polyfit(x, y, 3)
model = np.poly1d(coef)
print(f"18點購物人數預測 : {model(18):.2f}")
print(f"20點購物人數預測 : {model(20):.2f}")

plt.plot(18, model(18), "-o", color="red")
plt.plot(20, model(20), "-o", color="red")
plt.plot(x, model(x) , color='red')

plt.scatter(x, y )
plt.title("網路購物調查")
plt.xlabel("時間")
plt.ylabel("購物人數")
plt.show()
# 18點購物人數預測 : 85.63
# 20點購物人數預測 : 92.62
