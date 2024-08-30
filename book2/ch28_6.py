# 用 decision_function() 繪製邊界線
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from joblib import dump

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# 建立10個點,5個為分類A,5個為分類B
X = np.array([[1, 2.5], [0.5, 2], [2, 2], [1.5, 1], [2.5, 1.3],
              [3, 3.5], [4.5, 3.5], [4, 4], [2.5, 4.5], [3.5, 3] ])
y = np.array(['A','A','A','A','A','B','B','B','B','B',])

# 建立線性 SVM 模型
svc = svm.SVC(kernel='linear')
svc.fit(X, y)

# 繪製點,A 'o', B '*'
for i, marker in zip(['A', 'B'], ['o', '*']):
    plt.scatter(X[y==i, 0], X[y==i, 1], marker=marker, label=i )

# 獲取當前的坐標軸對象
ax = plt.gca()

# 建立格點評估模型
# np.linspace() 傳回平均間隔數字
xx = np.linspace(0, 5)  # array 50
yy = np.linspace(0, 5)  # array 50
XX, YY = np.meshgrid(xx, yy)    ## XX: 50*50 YY:50*50
# ravel() 方法將二維陣列壓平成一維陣列
# vstack() 將多個一維陣列在垂直方向上進行堆疊，生成一個新的 2D 陣列
# XX.ravel():2500, YY.ravel():2500
# np.vstack([XX.ravel(), YY.ravel()]) : 2 * 2500
# xy: 2500 * 2
xy = np.vstack([XX.ravel(), YY.ravel()]).T
# print(f"shap={xx.shape} xx={xx}")
# print(f"shap={XX.shape} XX={XX}")
# print(f"shap={YY.shape} YY={YY}")
# print(f"shap={XX.ravel().shape} XX.ravel()={XX.ravel()}")
# print(f"shap={xy.shape} xy={xy}")

# 傳回距超平面的距離
Z = svc.decision_function(xy).reshape(XX.shape)
# print(f"shap={svc.decision_function(xy).shape} xy={svc.decision_function(xy)}")
# print(f"shap={Z.shape} xy={Z}")

# 繪製決策邊和間隔
# 繪製 2D 等高線, -1 , 0, 1
ax.contour(XX, YY, Z, colors='b', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])

# 用圓圈繪製支援向量
# s=100 設置每個散點的大小
# facecolors='none', 'none' 表示點沒有填充顏色
# edgecolors='k', 設置點的邊界顏色 'k' 是黑色的縮寫
plt.scatter(svc.support_vectors_[:,0], svc.support_vectors_[:,1],
            s=100, facecolors='none', edgecolors='k')

plt.title('支援向量機-繪製超平面及決策邊界')
plt.xlabel(r'$x_{1}$', fontsize=14)
plt.ylabel(r'$x_{2}$', fontsize=14)
plt.legend()
plt.show()

