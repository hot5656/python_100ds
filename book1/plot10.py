# 欄列排列多張圖
# subplot(橫列數,直欄數,圖表索引)
import matplotlib.pyplot as plt

# 上下圖
# subplot(2,1,1)
# subplot(2,1,2)
plt.figure(figsize=[8,8])
# fig 1
plt.subplot(2,1,1)
plt.title(label='#1 Chat 1')
plt.plot([1,2,3], 'r:o')
# fig 2
plt.subplot(2,1,2)
plt.title(label='#1 Chat 2')
plt.plot([1,2,3], 'g--o')

# 左右圖
# subplot(1,2,1) subplot(1,2,2)
plt.figure(figsize=[8,8])
# fig 1
plt.subplot(1,2,1)
plt.title(label='#2 Chat 1')
plt.plot([1,2,3], 'r:o')
# fig 2
plt.subplot(1,2,2)
plt.title(label='#2 Chat 2')
plt.plot([1,2,3], 'g--o')

# 四張圖
# subplot(2,2,1) subplot(2,2,2)
# subplot(2,2,3) subplot(2,2,4)
plt.figure(figsize=[8,8])
# fig 1
plt.subplot(2,2,1)
plt.title(label='#3 Chat 1')
plt.plot([1,2,3], 'r:o')
# fig 2
plt.subplot(2,2,2)
plt.title(label='#3 Chat 2')
plt.plot([1,2,3], 'g--o')
# fig 3
plt.subplot(2,2,3)
plt.title(label='#3 Chat 3')
plt.plot([1,2,3], 'b:o')
# fig 4
plt.subplot(2,2,4)
plt.title(label='#3 Chat 4')
plt.plot([1,2,3], 'y--o')
plt.show()