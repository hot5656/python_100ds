# 繪製實際房價與預估房價
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
print(f"真實房價\n {np.array(y_test.tolist())}")
print("-"*70)
print(f"預測房價\n {y_pred.round(1)}")

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

plt.scatter(y_test, y_pred)
line_x = np.linspace(0, 50, 100)
plt.plot(line_x, line_x, color='red')
plt.title("實際房價vs預測房價")
plt.xlabel("實際房價")
plt.ylabel("預測房價")
plt.show()

# 真實房價
#  [28.2 23.9 16.6 22.  20.8 23.  27.9 14.5 21.5 22.6 23.7 31.2 19.3 19.4
#  19.4 27.9 13.9 50.  24.1 14.6 16.2 15.6 23.8 25.  23.5  8.3 13.5 17.5
#  43.1 11.5 24.1 18.5 50.  12.6 19.8 24.5 14.9 36.2 11.9 19.1 22.6 20.7
#  30.1 13.3 14.6  8.4 50.  12.7 25.  18.6 29.8 22.2 28.7 23.8  8.1 22.2
#   6.3 22.1 17.5 48.3 16.7 26.6  8.5 14.5 23.7 37.2 41.7 16.5 21.7 22.7
#  23.  10.5 21.9 21.  20.4 21.8 50.  22.  23.3 37.3 18.  19.2 34.9 13.4
#  22.9 22.5 13.  24.6 18.3 18.1 23.9 50.  13.6 22.9 10.9 18.9 22.4 22.9
#  44.8 21.7 10.2 15.4]
# ----------------------------------------------------------------------
# 預測房價
#  [28.6 28.2 17.5 23.8 20.1 24.1 29.5 21.5 17.7 25.8 28.  30.7 19.5 22.
#  22.1 20.  17.4 39.  25.6  5.4 20.8 17.1 26.2 27.6 28.  13.2 16.8 22.8
#  31.8 13.2 28.7 15.8 37.1 20.  24.4 20.4 19.5 31.4  5.9 20.4 26.4 26.7
#  27.5 14.6 18.7 18.5 36.6 18.4 23.7 24.6 26.5 24.  28.2 23.9  6.  27.4
#   9.3 26.3 20.  37.3 21.7 28.3 15.4 19.7  7.6 30.9 38.7 26.5 22.9 21.4
#  27.1  5.  15.8 24.9 21.  21.8 32.4 26.4 27.2 32.6 21.5 23.  31.6 17.2
#  28.  28.  18.9 28.3 19.5 20.1 30.4 38.6 17.7 21.6 21.1 21.  26.  26.4
#  37.3 22.  18.6 19.5]
