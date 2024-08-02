# 喜好電影預測
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# 電影數據(韓兩個特徵)
movies = np.array([
    [8, 7],     # 動作片
    [9, 8],     # 動作片
    [10, 9],    # 動作片
    [7, 6],     # 動作片
    [1, 2],     # 喜劇片
    [2, 1],     # 喜劇片
    [3, 4]     # 喜劇片
])

# 電影類型(0:動作片,1:喜劇片)
lables = np.array([0, 0, 0, 0, 1, 1, 1])

# 建立模型,進行訓練
# n_neighbors=3 取最近 3 點
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(movies, lables)

# Kwei 喜好電影類型-特徵 [6, 7]
kwei_movie = np.array([6, 7]).reshape(1,-1)

# 預測 Kwei 電影類型
prediction = knn.predict(kwei_movie)

if prediction == 0:
    print("推薦 Kwei 動作片")
else:
    print("推薦 Kwei 喜劇片")

# 推薦 Kwei 動作片