# 使用 numpy binomial 產生業務分析資料繪圖
import matplotlib.pyplot as plt
import numpy as np
# pip install seaborn
import seaborn as sns

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

n = 5
success = 0.75
# 修改次數及成功率
# n = 10
# success = 0.35
# numpy.random.binomial 函數用於生成來自二項式分布的隨機樣本
# n 次獨立試驗中，成功 k 次的可能性，每次試驗成功的概率為 𝑝, siz為生成資料數量
samples = np.random.binomial(n=n , p=success, size=1000)
# print(len(samples))
# print(samples)
# kde=True 會劃出核密度估計曲線
sns.histplot(samples, kde=False)
plt.title(f'銷售機率分析 Binomial ={n} 成功率:{success}')
plt.xlabel('銷售成功數')
plt.ylabel('成功次數')
plt.show()