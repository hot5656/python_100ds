# 繪製散點圖
import pandas as pd
import matplotlib.pyplot as plt

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')

# 建立兩個子圖畫布
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

# 繪第1個子圖
axs[0].scatter(boston['LSTAT'], boston['MEDV'])
axs[0].set_title("低收入比例vs房價")
axs[0].set_xlabel("低收入比例")
axs[0].set_ylabel("房價")
# 繪第2個子圖
axs[1].scatter(boston['RM'], boston['MEDV'])
axs[1].set_title("房間數vs房價")
axs[1].set_xlabel("房間數")
axs[1].set_ylabel("房價")

plt.show()



