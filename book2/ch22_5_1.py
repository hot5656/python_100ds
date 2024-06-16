# 數據中心點變成 (0,0)
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

X, y = make_blobs(n_samples=200, n_features=2, centers=2, random_state=0)

X_sta = StandardScaler().fit_transform(X)

# 建立兩個子圖畫布
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

axs[0].scatter(X[:,0], X[:,1], c=y)
axs[0].set_title("一般數據")
axs[0].grid()

axs[1].scatter(X_sta[:,0], X_sta[:,1], c=y)
axs[1].set_title("標準化數據")
axs[1].grid()

plt.show()

