from sklearn.metrics import classification_report

y_true = [1, 1, 0, 1, 0, 0, 1]
y_pred = [1, 0, 1, 1, 1, 0, 1]
report = classification_report(y_true, y_pred)
print("分類報告 :")
print(report)
# 分類報告 :
#               precision    recall  f1-score   support
#            0       0.50      0.33      0.40         3
#            1       0.60      0.75      0.67         4
#     accuracy                           0.57         7
#    macro avg       0.55      0.54      0.53         7
# weighted avg       0.56      0.57      0.55         7