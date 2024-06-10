# uniform(low, high, size) 平均分布的隨機函數
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# s = np.random.uniform(size=10000)
s = np.random.random(10000)

plt.hist(s, 30, density=True)
sns.kdeplot(s)
# plt.title("np.random.uniform 繪圖")
plt.title("np.random.random 繪圖")
plt.show()