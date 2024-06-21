from sklearn.metrics import confusion_matrix

y_true = [1, 1, 0, 1, 0, 0, 1]
y_pred = [1, 0, 1, 1, 1, 0, 1]
cm = confusion_matrix(y_true, y_pred)
print("混淆矩陣 :")
print(cm)
# 混淆矩陣 :
# [[1 2]
#  [1 3]]