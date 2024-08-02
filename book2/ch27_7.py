# KNN迴歸應用 - 房價預估2
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# 訓練數據(坪)
X_train = np.array([[50,15], [80,10], [120,5], [150,3],
                    [200,2], [250,1], [300,0.5]])
# 目標數值(價格萬元)
y_train = np.array([180, 280, 360, 420, 580, 720, 850])

# 建立模型 k=3, 擬合模型
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)

# 預測新的房子價格
X_new = np.array([[180, 7]])
y_pred = knn.predict(X_new)

# 輸出結果
print(f"{X_new[0,0]}坪 {X_new[0,1]}年的房子預估價格為 {y_pred[0]:.2f} 萬元")

# 180坪 7年的房子預估價格為 453.33 萬元