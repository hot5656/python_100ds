import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')

X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns=['LSTAT', 'RM'])
y = boston['MEDV']

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=1)

# 建立線性迴歸模型及擬合數據
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"真實房價\n {y_test.tolist()}")
print("-"*70)
print(f"預測房價\n {y_pred.round(1)}")

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

plt.scatter(y_test, y_pred)
plt.title("實際房價vs預測房價")
plt.xlabel("實際房價")
plt.ylabel("預測房價")
plt.show()


