# 簡單例子
from sklearn.neighbors import KNeighborsClassifier

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

# 建立模型,進行訓練
# n_neighbors=3 取最近 3 點
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

x = 1.1
print(f"x={x} 分類是  :{knn.predict([[x]])}")
print(f"x={x} 分類機率:{knn.predict_proba([[x]])}")

x = 1.6
print(f"x={x} 分類是  :{knn.predict([[x]])}")
print(f"x={x} 分類機率:{knn.predict_proba([[x]])}")

# x=1.1 分類是  :[0]
# x=1.1 分類機率:[[0.66666667 0.33333333]] - 0 的機率 0.66, 1 的機率 0.33
# x=1.6 分類是  :[1]
# x=1.6 分類機率:[[0.33333333 0.66666667]] - 3 的機率 0.33, 1 的機率 0.66