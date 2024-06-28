from joblib import load

model = load('bank_ch24_1_2.joblib')
age = eval(input("請輸入年齡 : "))
income = eval(input("請輸入年收入 :"))
debt = eval(input("請輸入債務 :"))

y_pred = model.predict([[age, income, debt]])
if y_pred[0] == 1:
    print("違規")
else:
    print("未違規")

# 請輸入年齡 : 50
# 請輸入年收入 :60000
# 請輸入債務 :1000
# 未違規
# 請輸入年齡 : 50
# 請輸入年收入 :60000
# 請輸入債務 :2000
# 違規