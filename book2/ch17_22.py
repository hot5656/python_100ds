# normal 產生常態分佈函數的隨機數(可設定平均值及標準差)
# normal 傳回實數,無特定range
# seaborn.kdeplot 繪製常態分佈曲線非常方便
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mu = 0
sigma = 1
s = np.random.normal(mu, sigma, 10000)

count, bins, ignored = plt.hist(s, 30, density=True)
# plt.plot(bins, 1/(sigma * np.sqrt( 2* np.pi)) * np.exp( -(bins - mu)**2 / (2*sigma**2)) , linewidth=2, color='r')
sns.kdeplot(s)
plt.show()