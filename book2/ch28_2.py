import numpy as np
from sklearn import svm

# 建立10個點,5個為分類A,5個為分類B
X = np.array([[1, 2.5], [0.5, 2], [2, 2], [1.5, 1], [2.5, 1.3],
              [3, 3.5], [4.5, 3.5], [4, 4], [2.5, 4.5], [3.5, 3] ])
y = np.array(['A','A','A','A','A','B','B','B','B','B',])

# 建立 linear svc+耦合
svc = svm.SVC(kernel='linear')
svc.fit(X, y)

# 支持向量 表 決策邊的向量
print(f'權重係數         :{svc.coef_}')
print(f'截距(偏置)       :{svc.intercept_}')
print(f'支持向量索引     :{svc.support_}')
print(f'支持向量         :\n{svc.support_vectors_}')
print(f'每個類別支援向量數:{svc.n_support_}')

# 權重係數         :[[0.79988954 0.80016569]]
# 截距(偏置)       :[-4.20015648]
# 支持向量索引     :[2 5 9]
# 支持向量         :[[2.  2. ]
#  [3.  3.5]
#  [3.5 3. ]]
# 每個類別支援向量數:[1 2]
#   w1 = 0.79988954
#   w2 = 0.80016569
#   d = -4.20015648