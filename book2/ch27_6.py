# KNN迴歸應用 - 房價預估
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# 訓練數據(坪)
X_train = np.array([50, 80, 120, 150, 200, 250, 300]).reshape(-1, 1)
# 目標數值(價格萬元)
y_train = np.array([180, 280, 360, 420, 580, 720, 850])

# 建立模型 k=3, 擬合模型
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)

# 預測新的房子價格
X_new = np.array([110]).reshape(-1, 1)
y_pred = knn.predict(X_new)

# 輸出結果
print(f"{X_new[0,0]}坪的房子預估價格為 {y_pred[0]:.2f} 萬元")

# 110坪的房子預估價格為 353.33 萬元
