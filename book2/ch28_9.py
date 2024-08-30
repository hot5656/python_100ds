# 3維 權重係數和截距
from sklearn.datasets import make_circles
from sklearn import svm
import numpy as np

# 生成數據
X, y = make_circles(n_samples=200, noise=0.05, random_state=10)
z = X[:,0]**2 + X[:,1]**2

features = np.concatenate((X, z.reshape(-1,1)), axis=1)
svc = svm.SVC(kernel='linear')
svc.fit(features, y)

print(f"權重係數  :{svc.coef_}")
print(f"截距(篇置):{svc.intercept_}")
# 權重係數  :[[-0.04930655  0.01521172 0.01523346]]
# 截距(篇置):[5.67719935]
# 權重係數  :[[-0.04930655  0.01521172 -6.89993346]]
# 截距(篇置):[5.67719935]
# 取小數四位
# w1 = -0.0493
# w2 = 0.0152
# w3 = -6.8999
# b = 5.6772
