import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data = {
    'height' : [162, 160, 167, 180, 177, 168, 189, 182, 176, 169],
    'waist'  : [ 71,  81,  70,  90,  95,  80,  78, 100,  84,  80],
    'weight' : [ 53,  62,  58,  71,  72,  69,  80,  91,  78,  70],
}

# 建立 DataFrmae
df = pd.DataFrame(data)
# 建立自變數和目標變數
X = df[['height', 'waist']]
y = df['weight']

# 分割測試數據與測試數據
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=1)

# 建立線性迴歸模型及擬合數據
model = LinearRegression()
model.fit(X_train, y_train)

# 查看模型的截距與係數
intercept = model.intercept_
coefficients = model.coef_
print(f"y截距(b0)  : {intercept:.3f}")
print(f"斜率(b1,b2): {coefficients.round(3)}")

# 組合線性迴歸方程式
formula = f"y = {intercept:.3f}"
for i, coef in enumerate(coefficients):
    formula += f" + ({coef:.3f})*x{i+1}"
print("線性迴歸方程式:")
print(formula)

# 算預測值
y_pred = model.predict(X_test)
# 計算 R 平方數
print(f"R2_Score:{r2_score(y_test, y_pred):.2f}")

# y截距(b0)  : -92.547
# 斜率(b1,b2): [0.71  0.482]
# 線性迴歸方程式:
# y = -92.547 + (0.710)*x1 + (0.482)*x2
# R2_Score:0.73