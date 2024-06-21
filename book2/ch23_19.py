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