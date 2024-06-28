# 繪製3D散點圖
import pandas as pd
import matplotlib.pyplot as plt

# windows 使用 微軟正黑體
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 顯示負號
plt.rcParams["axes.unicode_minus"] = False

# boston data url : http://lib.stat.cmu.edu/datasets/boston
boston = pd.read_csv("boston.csv", sep='\s+')

# 畫單張圖
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 繪製 3D 圖
ax.scatter(boston['LSTAT'], boston['RM'], boston['MEDV'], color='b')  # 散佈圖

# set title
ax.set_title('3D散點圖', fontsize=16, color='b')
# set label
ax.set_xlabel('低收入比例', color='g')
ax.set_ylabel('房間數', color='g')
ax.set_zlabel('房價', color='g')

plt.show()