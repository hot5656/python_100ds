# 計算樣本到決策邊界(超平面)的距離
from sklearn import svm

# 特徵數據: 重量,顏色
X = [ [150, 1], [170, 1], [130, 2], [140, 2],
      [200, 3], [210, 3], [180, 3], [220, 3]]

# 標籤數據
y = ['蘋果','蘋果','蘋果','蘋果',
     '橘子','橘子','橘子','橘子']

# 創建並訓練SVM分類器
clf = svm.SVC()
clf.fit(X, y)

# 使用訓練好的分類器來預測新的樣本
print(f"預測[160,1] 是 : {clf.predict([[160,1]])[0]}")
print(f"預測[190,3] 是 : {clf.predict([[190,3]])[0]}")

# 輸出一個數值,表示樣本到超平面的距離
# decision_function() 傳回距超平面的距離
print(f"[160,1] 到超平面的距離 : {clf.decision_function([[160,1]])[0]}")
print(f"[190,3] 到超平面的距離 : {clf.decision_function([[190,3]])[0]}")
print(f"[250,3] 到超平面的距離 : {clf.decision_function([[250,3]])[0]}")

# 預測[160,1] 是 : 蘋果
# 預測[190,3] 是 : 橘子
# [160,1] 到超平面的距離 : 0.3718262578491399
# [190,3] 到超平面的距離 : -0.3712206727264994
# [250,3] 到超平面的距離 : -1.3454929221350937