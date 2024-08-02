# 足球進球分析
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# distance 距離, angle 角度, goal 1=進球
distance = [10, 20, 10, 30, 20, 30, 15, 25, 20, 15]
angle = [30, 45, 60, 30, 60, 75, 45, 60, 70, 90]
goal = [1, 1, 0, 1, 0, 0, 1, 0, 0, 1]

# 整理數據
# 1D array 合成 2D array
X = np.column_stack((distance, angle))
y = np.array(goal)

# 建立模型,進行訓練
# n_neighbors=3 取最近 3 點
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# 輸入球員數據
new_distance = float(input("輸入射門距離(公尺):"))
new_angle = float(input("輸入射門角度:"))
new_player = np.array([[new_distance, new_angle]])

# 預測是否能進球
prediction = knn.predict(new_player)
prediction_proba = knn.predict_proba(new_player)

# 輸出結果
print(f"是否進球(0沒進,1進球):{prediction}")
print(f"不進球機率: {prediction_proba[0][0]:.3f}")
print(f"進球  機率: {prediction_proba[0][1]:.3f}")

# 輸入射門距離(公尺):36
# 輸入射門角度:63
# 是否進球(0沒進,1進球):[0]
# 不進球機率: 1.000
# 進球  機率: 0.000
#
# 輸入射門距離(公尺):35
# 輸入射門角度:48
# 是否進球(0沒進,1進球):[1]
# 不進球機率: 0.333
# 進球  機率: 0.667
