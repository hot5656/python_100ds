from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 生成數據
X, y = make_regression(n_features=1, noise=20, random_state=10)

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=10)

# 建立線性回歸模型
model = LinearRegression()
# 數據擬合模型 model.fit(X=height, y=weight) 做數據擬合, X必需為二維陣列
model.fit(X=X_train, y=y_train)

# 繪資料圖
plt.scatter(X_train, y_train, label="訓練數據")
plt.scatter(X_test, y_test, label="測試數據")

# 繪迴歸線
y_pred = model.predict(X_test)
plt.plot(X_test, y_pred, color='red')

# 計算 R 平方數
print(f"R2_Score:{r2_score(y_test, y_pred):.2f}")

plt.legend()
plt.axis([-3, 3, -150, 150])
plt.show()
# R2_Score:0.76