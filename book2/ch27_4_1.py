from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# make_blobs 是 Scikit-learn 庫中用於生成合成數據集的函數
# 這個函數主要用於創建聚類算法的測試數據集
# 主要參數和返回值
#   n_samples: 要生成的樣本數。
#   centers: 簇的中心數量或具體坐標。如果是整數，則隨機生成指定數量的簇中心；如果是數組，則使用提供的坐標作為簇中心。
#   n_features: 每個樣本的特徵數。即每個數據點的維度。
#   cluster_std: 每個簇的標準差。可設置單一值或數組，數組時可為每個簇指定不同的標準差。
#   random_state: 用於確保生成的數據集的一致性，方便重現結果。
# 返回值
#   X: 包含數據點的數組，每行是一個數據點。
#   y: 每個數據點所屬簇的標籤數組。
# 生成數據
X, y = make_blobs(n_samples=200, centers=2, random_state=8)

# print(f"X={X}")
# print(f"y={y}")
# 顯示散點圖
plt.scatter(X[:,0], X[:,1], c=y, edgecolor='b')

plt.show()
