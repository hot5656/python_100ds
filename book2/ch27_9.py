from sklearn import datasets

# load 鳶尾花數據
iris = datasets.load_iris()
print(f"自變數  樣本外形 : {iris.data.shape}")
print(f"目標變數樣本外形 : {iris.target.shape}")

# 特徵名稱
print(f"特徵名稱\n {iris.feature_names}")

# 描述特徵名稱
print(f"描述特徵名稱\n {iris.DESCR}")

# 自變數  樣本外形 : (150, 4)
# 目標變數樣本外形 : (150,)
# 特徵名稱
#  ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# 描述特徵名稱
#  .. _iris_dataset: