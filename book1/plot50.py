# 圖書分類銷售分析圖
import matplotlib.pyplot as plt
# 加入中文字體
import matplotlib
from matplotlib.font_manager import fontManager
# 加入中文字體
fontManager.addfont('NotoSansTC-Regular.ttf')
matplotlib.rc('font', family='Noto Sans TC')

listx = ['商業理財','文學小說','藝術設計','人文科普','電腦語言','心靈養生','生活風格','親子共享']
listm = [0.14,0.16,0.08,0.13,0.16,0.12,0.16,0.05]
listf = [0.1,0.19,0.06,0.1,0.13,0.13,0.2,0.09]
listm = [x*100 for x in listm]
listf = [x*100 for x in listf]

# plt.figure(figsize=[12,9])
# plt.subplot(2,2,1)
plt.figure(figsize=(12,9))
plt.subplot(221)
plt.title(label='分類比率-男性')
plt.pie(listm, labels=listx, autopct = '%2.1f%%',)

# plt.subplot(2,2,2)
plt.subplot(222)
plt.title(label='分類比率-女性')
plt.pie(listf, labels=listx, autopct = '%2.1f%%',)

# plt.subplot(2,2,3)
plt.subplot(223)
plt.title(label='分類長條圖')
width1 = 0.4
listx1 = [x - width1/2 for x in range(len(listx))]
listx2 = [x + width1/2 for x in range(len(listx))]
plt.bar(listx1, listm, width1)
plt.bar(listx2, listf, width1)
# x軸 標示 旋轉
plt.xticks(range(len(listx)), labels=listx, rotation=45)

plt.xlabel('圖書分類', fontsize=12)
plt.ylabel('銷售比率(%)', fontsize=12)
plt.legend()

# plt.subplot(2,2,4)
plt.subplot(224)
plt.title(label='分類長折線圖')
plt.plot(listx, listm, marker='s' ,label='男')
plt.plot(listx, listf, marker='s' ,label='女')
plt.grid(True)
plt.xticks(rotation=45)
plt.xlabel('圖書分類', fontsize=12)
plt.ylabel('銷售比率(%)', fontsize=12)
# x軸 標示 旋轉
plt.legend()

plt.show()
