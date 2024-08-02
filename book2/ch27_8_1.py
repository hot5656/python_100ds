import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

# 生成線性數據
# make_regression 用於生成合成線性回歸數據集的函數
# 主要參數
#   n_samples（樣本數量）：指定要生成的數據點數量。默認值為 100。
#   n_features（特徵數量）：每個數據點的特徵數量。在回歸問題中，這表示自變量的個數。
#   n_informative（有用特徵數量）：對於回歸任務有實際影響的特徵數量。默認值是 n_features。
#   noise（噪聲）：目標變量中添加的高斯噪聲的標準差。這個參數用來模擬數據中的隨機誤差或不確定性。
#   random_state（隨機種子）：用於控制生成數據集的隨機性。設置這個值可以保證每次生成相同的數據集，方便結果重現。
# 返回值
#   X：生成的特徵數據集，是一個形狀為 (n_samples, n_features) 的二維數組。
#   y：對應的目標變量，是一個形狀為 (n_samples,) 的一維數組。
X, y = make_regression(n_features=1, noise=20, random_state=10)

plt.scatter(X, y, c='y', edgecolors='b')
plt.show()