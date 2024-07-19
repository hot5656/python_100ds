import pandas as pd
import matplotlib.pyplot as plt

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 讀取糖尿病數據
df = pd.read_csv('new_diabetes.csv')

plt.hist(df['Glucose'], bins=10, edgecolor='black')

plt.xlabel('血糖值')
plt.ylabel('人數')
plt.title('血糖分佈')
plt.show()