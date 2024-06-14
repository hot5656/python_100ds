# 不適合三次函數迴歸數據(實例)
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,
     12,13,14,15,16,17,19,21,22,23,24]
y = [100, 21, 75, 49, 15, 98, 55, 31, 33, 82, 61,
      80, 32, 71, 99, 15, 66, 88, 21, 97, 30, 5]

coef = np.polyfit(x, y, 3)
model = np.poly1d(coef)
print(f"MSE:{mean_squared_error(y, model(x)):.3f}")
print(f"R2_Score:{r2_score(y, model(x)):.3f}")

plt.plot(x, model(x) , color='red')

plt.scatter(x, y )
plt.title("網路購物調查")
plt.xlabel("時間")
plt.ylabel("購物人數")
plt.show()
# 適合三次函數
# MSE:14.803
# R2_Score:0.944
# 不適合三次函數
# MSE:813.885
# R2_Score:0.151