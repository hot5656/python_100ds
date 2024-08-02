# 計算最優k值 (k<43 有較好的準確度)
from sklearn import datasets
# import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
# import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#  windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# load 鳶尾花數據
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 分割訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                    test_size=0.1, random_state=42)

# 設定所有準確度列表
accuracy_scores = []

k_values = list(range(1, 100, 2))
for k in k_values:
    # 建立模型,進行訓練
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)
    # 計算準確度
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_scores.append(accuracy)
    print(f'k={k}, 準確度: {accuracy:.3f}')

# 繪製圖表
plt.figure()
plt.plot(k_values, accuracy_scores, marker='o')
plt.title('鳶尾花預估準確值 vs k值')
plt.xlabel('k 值')
plt.ylabel('準確度')
plt.grid(True)
plt.show()

# k=1, 準確度: 1.000
# k=3, 準確度: 1.000
# k=5, 準確度: 1.000
# k=7, 準確度: 0.933
# k=9, 準確度: 1.000
# k=11, 準確度: 1.000
# k=13, 準確度: 1.000
# k=15, 準確度: 1.000
# k=17, 準確度: 1.000
# k=19, 準確度: 1.000
# k=21, 準確度: 1.000
# k=23, 準確度: 1.000
# k=25, 準確度: 1.000
# k=27, 準確度: 1.000
# k=29, 準確度: 1.000
# k=31, 準確度: 1.000
# k=33, 準確度: 1.000
# k=35, 準確度: 1.000
# k=37, 準確度: 1.000
# k=39, 準確度: 1.000
# k=41, 準確度: 1.000
# k=43, 準確度: 1.000
# k=45, 準確度: 0.933
# k=47, 準確度: 0.933
# k=49, 準確度: 0.933
# k=51, 準確度: 1.000
# k=53, 準確度: 1.000
# k=55, 準確度: 1.000
# k=57, 準確度: 0.933
# k=59, 準確度: 0.933
# k=61, 準確度: 0.933
# k=63, 準確度: 0.933
# k=65, 準確度: 0.933
# k=67, 準確度: 0.933
# k=69, 準確度: 0.933
# k=71, 準確度: 0.933
# k=73, 準確度: 0.933
# k=75, 準確度: 0.933
# k=77, 準確度: 0.933
# k=79, 準確度: 0.933
# k=81, 準確度: 0.933
# k=83, 準確度: 0.933
# k=85, 準確度: 0.933
# k=87, 準確度: 0.933
# k=89, 準確度: 0.733
# k=91, 準確度: 0.733
# k=93, 準確度: 0.733
# k=95, 準確度: 0.733
# k=97, 準確度: 0.733
# k=99, 準確度: 0.733