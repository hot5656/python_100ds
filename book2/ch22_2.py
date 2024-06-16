# 繪製多子圖
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# 生成數據
X1, y1 = make_regression(n_features=1, noise=0, random_state=10)
X2, y2 = make_regression(n_features=1, noise=10, random_state=10)

# 建立兩個子圖畫布
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
# 繪第1個子圖
axs[0].scatter(X1, y1)
axs[0].set_title("Noise = 0")
# 繪第2個子圖
axs[1].scatter(X2, y2)
axs[1].set_title("Noise = 10")
# 設定標籤
for ax in axs:
    ax.set_xlabel("特徵")
    ax.set_ylabel("目標")

# 自動調整子圖間距
plt.tight_layout()
plt.show()

