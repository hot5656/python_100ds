import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, roc_curve

y_true = [0, 0, 1, 1]
y_scores = [0.1, 0.4, 0.35, 0.8]
auc_score = roc_auc_score(y_true, y_scores)
print(f"ROC AUC 分數 : {auc_score}")
# ROC AUC 分數 : 0.75

# 計算FPR和TPR
fpr, tpr, thresholds = roc_curve(y_true, y_scores)
print(f"fpr={fpr}")
print(f"tpr={tpr}")
print(f"thresholds={thresholds}")
# fpr=[0.  0.  0.5 0.5 1. ]
# tpr=[0.  0.5 0.5 1.  1. ]
# thresholds=[ inf 0.8  0.4  0.35 0.1 ]


# 繪製ROC曲線
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {auc_score:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')

# 標示出梯形的面積區域
for i in range(1, len(fpr)):
    plt.fill_betweenx([0, tpr[i]], fpr[i-1], fpr[i], color='orange', alpha=0.3)

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc='lower right')
plt.show()