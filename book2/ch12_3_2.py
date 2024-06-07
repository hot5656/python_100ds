import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 設定參數
n = 5
p = 0.75
size = 1000

# 生成樣本
samples = np.random.binomial(n, p, size)

# 繪製直方圖，不包含核密度估計曲線
sns.histplot(samples, kde=False)
plt.title('Histogram without KDE')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.show()

# 繪製直方圖，包含核密度估計曲線
sns.histplot(samples, kde=True)
plt.title('Histogram with KDE')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.show()