from joblib import load

# 載入模型
svc = load('svc28_3.joblib')

while(1):
    x = eval(input("請輸入 x 座標:"))
    y = eval(input("請輸入 y 座標:"))
    print(f"({x},{y}) 分類是:{svc.predict([[x,y]])[0]}")
    z = input(f'是否繼續(y/n) : ')
    if z == 'n' or z == 'N':
        break

# 請輸入 x 座標:3
# 請輸入 y 座標:3
# (3,3) 分類是:B
# 是否繼續(y/n) : y
# 請輸入 x 座標:2
# 請輸入 y 座標:2
# (2,2) 分類是:A