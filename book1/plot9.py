# 設定圖表區
import matplotlib.pyplot as plt

# 第一張圖
plt.figure
plt.plot([1,2,3])

# 第二張圖
# figsize [寬,高](inches)
# dpi 解析度
# facecolor 背景顏色
# edgecolor 邊緣顏色
# linewidth 邊線寬度
# frameon 是否有邊框
plt.figure(
    figsize=[10,4],
    facecolor='whitesmoke',
    edgecolor='r',
    linewidth=10,
    frameon=True
)
plt.plot([1,2,3])
plt.show()
