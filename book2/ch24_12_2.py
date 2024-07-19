import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 讀取糖尿病數據
df = pd.read_csv('new_diabetes.csv')

titles = ['懷孕次數','血糖值','血壓','皮膚厚度','胰島素',
          'BMI','糖尿病家族函數','年齡','是否有糖尿病']

fig = plt.figure(figsize=(15,10))
for i, col in enumerate(df.columns, 1):
    ax = fig.add_subplot(3, 3, i)
    sns.boxplot(y=df[col], ax=ax)
    ax.set_title(titles[i-1], fontsize=14)

plt.subplots_adjust(wspace=0.3, hspace=0.5)
plt.show()