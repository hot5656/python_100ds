# 造勢烤香腸預估
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# 訓練數據
X_train = np.array([[0, 3, 3], [2, 4, 3], [2, 5, 6], [1, 4, 2],
                    [2, 3, 1], [1, 5, 4], [0, 1, 1], [2, 4, 3],
                    [2, 2, 4], [1, 3, 5], [1, 5, 5], [2, 5, 1]])
# 目標數值
y_train = np.array([100, 250, 350, 180, 170, 300, 50,
                    275, 230, 165, 320, 210])

# 建立模型 k=5, 擬合模型
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)

# 預測準備香腸數
X_new = np.array([[1, 5, 2]])
y_pred = knn.predict(X_new)

# 輸出結果
print(f"應該準備 {int(y_pred[0])} 條香腸")

# 應該準備 243 條香腸