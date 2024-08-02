from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load 鳶尾花數據
iris = datasets.load_iris()

# 將數據轉成 DataFrame format
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# 轉鳶尾花數據為標籤
df['species'] = df['species'].map({0:'setosa', 1:'versicolor', 2:'virginica'})

#  windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# seaborn 是一個基於 matplotlib 的 Python 資料視覺化庫，旨在提供更高層次的界面來繪製統計圖表。
# sns.scatterplot() 特別用於繪製散點圖，其主要目的是展示兩個變量之間的關係或分佈情況。每個數據點在圖上對應於資料集中一組特定的 x 和 y 座標值。
# 主要參數說明
#     x 和 y: 定義散點圖的 X 軸和 Y 軸資料。這些資料可以是資料框（DataFrame）中的列名，指定要繪製的變量。
#     data: 資料來源，通常是一個 pandas 資料框（DataFrame）。這個參數指定了要繪製圖表的數據集合。
#     hue: 用於根據某一類別變量的值對數據點進行著色，以便在圖中視覺上區分不同的組別。
#     style: 根據某一類別變量的值改變數據點的形狀，以區分不同的類別。
#     size: 根據某一數值變量的大小改變數據點的大小。
#     palette: 定義數據點顏色的調色板，可以是內置的顏色列表或自定義顏色列表。
#     markers: 設置不同組別的數據點標記樣式，可以指定具體的標記形狀。
#     alpha: 控制數據點的透明度，取值範圍為 0 到 1，0 為完全透明，1 為完全不透明。
# 傘點圖
sns.scatterplot(data=df, x='sepal length (cm)', y = 'sepal width (cm)', style='species', hue='species')
plt.title("花萼長度(sepal length) vs 花萼寬度(sepal width)")
plt.show()