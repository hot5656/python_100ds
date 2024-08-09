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

# 繪製點,A 'o', B '*'
for i, marker in zip(['A', 'B'], ['o', '*']):
    plt.scatter(X[y==i, 0], X[y==i, 1], marker=marker, label=i )

# 建立 linear svc+耦合
svc = svm.SVC(kernel='linear')
svc.fit(X, y)

# 權重, 偏置值
w = svc.coef_[0]
slope = -w[0] / w[1]
b = svc.intercept_[0]
# 儲存模型
dump(svc, 'svc28_3.joblib')

# 繪製超平面
xx = np.linspace(0, 5)
# same as yy = (-b - w[0] * xx)/w[1], but use slope
# yy_slope = slope * xx - ( b / w[1])
yy = (-b - w[0] * xx)/w[1]
plt.plot(xx, yy, linewidth=2, color='green')

# 繪製邊界1
sv = svc.support_vectors_[0]
# b = -(w[0]*sv[0] + w[1]*sv[1])
yy_1 = ((w[0]*sv[0] + w[1]*sv[1]) - w[0] * xx)/w[1]
plt.plot(xx, yy_1, 'b--')

# 繪製邊界2
sv = svc.support_vectors_[-1]
yy_2 = ((w[0]*sv[0] + w[1]*sv[1]) - w[0] * xx)/w[1]
plt.plot(xx, yy_2, 'b--')

# xx = np.linspace(0, 5)
# same as yy = (-b - w[0] * xx)/w[1], but use slope
# yy_slope = slope * xx - ( b / w[1])
# yy = (-b - w[0] * xx)/w[1]
# plt.plot(xx, yy, linewidth=2, color='green')

# 用圓圈繪製支援向量
# s=100 設置每個散點的大小
# facecolors='none', 'none' 表示點沒有填充顏色
# edgecolors='k', 設置點的邊界顏色 'k' 是黑色的縮寫
plt.scatter(svc.support_vectors_[:,0], svc.support_vectors_[:,1],
            s=100, facecolors='none', edgecolors='k')

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.title('支援向量機-繪製超平面及決策邊界')
plt.xlabel(r'$x_{1}$', fontsize=14)
plt.ylabel(r'$x_{2}$', fontsize=14)
plt.legend()
plt.show()