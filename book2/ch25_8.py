import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from graphviz import Source
from sklearn.metrics import confusion_matrix

# load 數據
titanic_data = sns.load_dataset('titanic')
# 選取有用特徵
titanic_data = titanic_data[['survived','pclass','sex']]

# 將 sex 轉位數字
sex_encoder = LabelEncoder()
# print(titanic_data['sex'])
sex_encoded = sex_encoder.fit_transform(titanic_data['sex'])
titanic_data['sex'] = sex_encoded
# print(titanic_data['sex'])
# male=1 female=0

# 分割數據為訓練集及測試集
X = titanic_data.drop('survived', axis=1)
y = titanic_data['survived']
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=5)

# 建立決策樹模型並進行訓練
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, y_train)

# 進行預測
y_pred = dt_classifier.predict(X_test)

# 預測結果比較
print("1表存活")
print(f"測試的真實分類\n{y_test.to_numpy()}")
print("-"*70)
print(f"測試的目標分類\n{y_pred}")
print("="*70)

# 準確率
print(f"準確率 : {dt_classifier.score(X_test, y_test):.2f}")

# 預測採集樣本為正類的機率
# AUC-ROC（Area Under the Receiver Operating Characteristic Curve）分數
# 是一種評估二分類模型性能的指標。它表示模型區分正類和負類的能力，範圍從0.0到
# 1.0，1.0表示完美區分，0.5表示隨機猜測。
# pre_rate[:,0]表為0的機率, pre_rate[:,0]表為1的機率
pre_rate = dt_classifier.predict_proba(X_test)
# 交叉分析表
print('1表female')
cross_tbl = pd.crosstab(pre_rate[:,0],
                columns=[X_test['pclass'], X_test['sex']])
print(cross_tbl)

#add feature name and class_names
feature_names = ['pclass','sex']
class_names = ['survived','dead']
grpah = Source(tree.export_graphviz(dt_classifier, out_file=None, feature_names=feature_names, class_names=class_names, filled=True))

grpah.format = 'png'
grpah.render(filename='dt_classifier_tree', view=True)

# 1表存活
# 測試的真實分類
# [0 0 0 1 0 0 1 1 1 0 0 0 1 1 0 1 1 0 0 0 0 1 1 1 0 0 1 1 0 0 0 1 1 1 1 1 0
#  1 0 0 0 1 1 1 0 0 1 1 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 0 0
#  0 0 0 0 1 1 0 0 0 0 1 1 0 1 0 1 0 0 1 0 1 0 1 0 0 0 1 0 0 0 1 1 0 0 0 1 0
#  0 0 1 1 1 1 1 1 1 1 1 0 1 0 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 1
#  0 1 1 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 1 0 0 0 1 0 1 1 0 0 0 1 0]
# ----------------------------------------------------------------------
# 測試的目標分類
# [0 0 0 0 0 0 1 0 1 0 0 0 0 1 0 1 0 1 0 0 0 1 1 1 0 0 0 0 0 0 0 0 1 0 1 0 0
#  0 0 0 0 1 0 0 0 0 1 1 0 0 1 1 1 0 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 0
#  1 0 0 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 1 0
#  0 1 0 1 1 1 0 1 1 1 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 1 0 1
#  0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 1 1 1 0 0 0 1 0 1 1 0 0 0 1 0]
# ======================================================================
# 準確率 : 0.79
# 1表female
# pclass     1       2       3
# sex        0   1   0   1   0   1
# row_0
# 0.027397  21   0   0   0   0   0
# 0.067797   0   0  17   0   0   0
# 0.495935   0   0   0   0  21   0
# 0.647619   0  17   0   0   0   0
# 0.835443   0   0   0  29   0   0
# 0.868132   0   0   0   0   0  74