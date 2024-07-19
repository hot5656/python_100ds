import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 讀取糖尿病數據
df = pd.read_csv('new_diabetes.csv')

df.columns = ['懷孕次數','血糖值','血壓','皮膚厚度','胰島素',
          'BMI','糖尿病家族函數','年齡','是否有糖尿病']

plt.figure(figsize=(12,10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm' )
plt.title('糖尿病特徵皮爾遜相關係數熱力圖')
plt.yticks(rotation=30)
plt.show()