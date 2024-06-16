from sklearn.datasets import make_blobs
import matplotlib.pylab as plt

X1 ,y1 = make_blobs(n_samples=500, n_features=2, centers=5, random_state=1)
X2 ,y2 = make_blobs(n_samples=300, n_features=2, centers=3, random_state=1)

# 建立兩個子圖畫布
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
# 繪第1個子圖
axs[0].scatter(X1[:,0], X1[:,1], c=y1)
axs[0].set_title("First dataset")
# 繪第2個子圖
axs[1].scatter(X2[:,0], X2[:,1], c=y2)
axs[1].set_title("Second dataset")

plt.show()