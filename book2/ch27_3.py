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

# 電影名稱
movie_names = np.array([
    "Mission Impossible",
    "搶救雷恩大兵",
    "玩命關頭",
    "雷神索爾",
    "真善美",
    "愛情停損點",
    "雙手的溫柔"
])

# 建立模型,進行訓練
# n_neighbors=3 取最近 3 點
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(movies, lables)

# Kwei 喜好電影類型-特徵 [8, 7]
kwei_movie = np.array([8, 7]).reshape(1,-1)

# 找出與 Kwei 電影喜好,最接近3部電影
distences, indices = knn.kneighbors(kwei_movie)
print(f"最接近喜好的距離: {distences}")
print(f"最接近喜好的索引: {indices}")
print("="*70)

# 多維陣列轉成list
index = indices.flatten()
print(index)

# 列出 Kwel 喜好最接近3部電影
print("列出 Kwel 喜好最接近3部電影")
for i in index:
    print(f"{movie_names[i]} {movies[i]}")

# 最接近喜好的距離: [[0.         1.41421356 1.41421356]]
# 最接近喜好的索引: [[0 1 3]]
# ======================================================================
# [0 1 3]
# 列出 Kwel 喜好最接近3部電影
# Mission Impossible [8 7]
# 搶救雷恩大兵 [9 8]
# 雷神索爾 [7 6]
