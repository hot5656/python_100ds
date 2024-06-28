# 一元一次迴歸公式
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data23_19.csv')

X = pd.DataFrame(df.x)
y = df.y

print(df)
print(X)
print(y)

model = LinearRegression()
model.fit(X,y)
y_pred = model.predict(X)
print(f"R2_score = {model.score(X, y):.3f}")

plt.plot(X, y_pred, color='g')
plt.scatter(df.x, df.y)
plt.show()

#    x    y
# 0  1  1.5
# 1  2  3.0
# 2  3  4.5
# 3  4  4.2
# 4  5  5.2
# 5  6  5.5
#    x
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5
# 5  6
# 0    1.5
# 1    3.0
# 2    4.5
# 3    4.2
# 4    5.2
# 5    5.5
# Name: y, dtype: float64
# R2_score = 0.880