# 設計機器學習模型,繪製所有變數的散點圖,也是認識數據特徵的好方法
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

# sns.pairplot() 主要用於資料探索（exploratory data analysis, EDA），
# 可以幫助分析師快速了解數據中的變量之間的關係、數據的分佈情況和潛在的相關性。
# 主要參數說明
#   data: 指定要繪製的資料框（DataFrame），這是必須提供的參數。
#   hue: 用於設置根據某個類別變量對數據點進行顏色區分。例如，可以使用顏色來區分不同的類別標籤。
#   vars: 指定要包括在圖中的變量列表。如果未指定，將使用資料框中的所有數值變量。
#   kind: 指定對角線上的圖形類型，可以是 "scatter"（散點圖）、"kde"（核密度估計）或 "hist"（直方圖）。默認為 "scatter"。
#   diag_kind: 指定對角線上的圖形類型，可以是 "auto"、"hist"（直方圖）或 "kde"（核密度估計）。默認為 "auto"，
#               這意味著 hue 變量是類別變量時顯示直方圖，否則顯示核密度估計。
#   palette: 設定調色盤，用於設置不同類別的顏色。
#   markers: 用於指定不同類別的數據點標記樣式。
#   plot_kws: 提供其他繪圖參數，這些參數會傳遞給底層的 seaborn 繪圖函數。
# 使用 pairplot 繪製 sepal length(花萼長度) 和 petal length(花瓣長度) 兩個特徵的圖形
# 繪兩個特徵
sns.pairplot(df, vars=['sepal length (cm)', 'petal length (cm)'], hue='species')
# 繪所有個特徵
sns.pairplot(df, hue='species')

plt.show()