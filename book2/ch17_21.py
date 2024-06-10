# randn產生1個或多個平均值是0,標準差是1的常態分佈隨機數
# randn傳回實數,無特定range
import matplotlib.pyplot as plt
import numpy as np

mu = 0
sigma = 1
s = np.random.randn(10000)

# density=True告訴plt.hist()函數要繪製一個標準化的直方圖
# density=True被設置，這些值被歸一化，因此它們表示每個區間中資料點的比例，而不是絕對數量
# bins是用於定義直方圖區間邊界的陣列。這些邊界包括了最小值到最大值之間的所有區間
# ignored：是一個無用的值，它在這個情況下沒有被使用，所以可以忽略它。
count, bins, ignored = plt.hist(s, 30, density=True)
print(f"{len(count)} count={count}")
print(f"{len(bins)},bins={bins}")
print(f"ignored={ignored}")
plt.plot(bins, 1/(sigma * np.sqrt( 2* np.pi)) * np.exp( -(bins - mu)**2 / (2*sigma**2)) , linewidth=2, color='r')
plt.show()
