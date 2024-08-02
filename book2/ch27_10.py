# pandas 顯示鳶尾花數據
from sklearn import datasets
import pandas as pd

# 顯示所有 columns
pd.set_option('display.max_columns', None)
# 設定顯示每 row 長度
pd.set_option('display.width', 200)

# load 鳶尾花數據
iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

print(df.head())

# 轉鳶尾花數據為標籤
df['species'] = df['species'].map({0:'setosa', 1:'versicolor', 2:'virginica'})
print(df.head())
print(df.groupby('species').size())

#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  species
# 0                5.1               3.5                1.4               0.2        0
# 1                4.9               3.0                1.4               0.2        0
# 2                4.7               3.2                1.3               0.2        0
# 3                4.6               3.1                1.5               0.2        0
# 4                5.0               3.6                1.4               0.2        0
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) species
# 0                5.1               3.5                1.4               0.2  setosa
# 1                4.9               3.0                1.4               0.2  setosa
# 2                4.7               3.2                1.3               0.2  setosa
# 3                4.6               3.1                1.5               0.2  setosa
# 4                5.0               3.6                1.4               0.2  setosa
# species
# setosa        50
# versicolor    50
# virginica     50
# dtype: int64

