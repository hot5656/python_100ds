from sklearn.preprocessing import LabelEncoder

fruits = ['apple', 'apple', 'chery', 'apple', 'chery', 'orange']
# 創建 LabelEncoder 物件
label = LabelEncoder()

# fit_transform 轉為數值
fruits_encoded = label.fit_transform(fruits)
print(fruits_encoded)

# inverse_transform 轉回原來文字
print(label.inverse_transform(fruits_encoded))
# [0 0 1 0 1 2]
# ['apple' 'apple' 'chery' 'apple' 'chery' 'orange']