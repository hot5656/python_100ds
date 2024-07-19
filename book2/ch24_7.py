from sklearn import datasets

wine = datasets.load_wine()
print(f"自變數 樣本外型 : {wine.data.shape}")
print(f"目標變數樣本外型 : {wine.target.shape}")

# 輸出特徵值名稱
print("自變數特徵值名稱")
print(wine.feature_names)

# 輸出三組自變數
print("自變數特徵值")
print(wine.data[:3])

# 輸出三組目標變數
print("目標變數特徵值")
print(wine.target[:3])

# 描述特徵值名稱
print("描述特徵值名稱")
print(wine.DESCR)

# 自變數 樣本外型 : (178, 13)
# 目標變數樣本外型 : (178,)
# 自變數特徵值名稱
# ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'maglavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'co0/od315_of_diluted_wines', 'proline']
# 自變數特徵值
# [[1.423e+01 1.710e+00 2.430e+00 1.560e+01 1.270e+02 2.800e
#   2.800e-01 2.290e+00 5.640e+00 1.040e+00 3.920e+00 1.065e
#  [1.320e+01 1.780e+00 2.140e+00 1.120e+01 1.000e+02 2.650e
#   2.600e-01 1.280e+00 4.380e+00 1.050e+00 3.400e+00 1.050e
#  [1.316e+01 2.360e+00 2.670e+00 1.860e+01 1.010e+02 2.800e
#   3.000e-01 2.810e+00 5.680e+00 1.030e+00 3.170e+00 1.185e
# 目標變數特徵值
# [0 0 0]
# 描述特徵值名稱
#     ...