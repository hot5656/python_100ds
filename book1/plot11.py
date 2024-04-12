# 相對位置排列多張圖
# axes([與左邊界距離,與下邊界距離,寬,高]) 寬,高 相對外框
import matplotlib.pyplot as plt

plt.figure(figsize=[8,4])
plt.axes([0.1,0.1,0.35,0.8])
plt.title(label='#1 Chat 1')
plt.plot([1,2,3], 'r:o')
plt.axes([0.6,0.1,0.35,0.8])
plt.title(label='#1 Chat 2')
plt.plot([1,2,3], 'g--o')

plt.figure(figsize=[8,4])
plt.axes([0.1,0.1,0.8,0.8])
plt.title(label='#2 Chat 1')
plt.plot([1,2,3], 'r:o')
plt.axes([0.55,0.2,0.2,0.2])
plt.title(label='#2 Chat 2')
plt.plot([1,2,3], 'g--o')

plt.show()


