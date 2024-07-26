import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 顯示所有 columns
pd.set_option('display.max_columns', None)
# 設定顯示每 row 長度
pd.set_option('display.width', 300)

# 讀取數據
sales_df = pd.read_csv('sales.csv')
features_df = pd.read_csv('features.csv')
stores_pd = pd.read_csv('stores.csv')

# 合併 features_df, sales_df, link key = 'Store' + 'Date'
merged_df = pd.merge(sales_df, features_df, on=['Store', 'Date'], how='left')
# 合併 stores_pd, link key = 'Store'
final_df = pd.merge(merged_df, stores_pd, on=['Store'], how='left')

# Date 轉為日期型數據
final_df['Date'] = pd.to_datetime(final_df['Date'], format='%d/%m/%Y')

# 提出年份及月份
final_df['Year'] = final_df['Date'].dt.year
final_df['Month'] = final_df['Date'].dt.month

# 將 Type 轉成類型數據
# 將 Type 列的資料類型轉換為 category 類型
# .cat.codes：將類別型資料轉換為對應的數字編碼。每個類別將被分配一個整數編碼（從0開始）
final_df['Type'] = final_df['Type'].astype('category').cat.codes

# print 區失值統計
# print(final_df.head())
# print(final_df.isnull().sum())

# 處理區失值
final_df.fillna(0, inplace=True)


# 刪除 IsHoliday_y, 將 IsHoliday_x 改為 IsHoliday
final_df = final_df.drop('IsHoliday_y', axis=1)
final_df = final_df.rename(columns={'IsHoliday_x': 'IsHoliday'})

# 將結果存為 RetailDataAnalytics.csv
final_df.to_csv('RetailDataAnalytics.csv', index=False)

# 定義特徵變量和目標變量
X = final_df.drop(['Weekly_Sales', 'Date'], axis=1)
y = final_df['Weekly_Sales']

# 劃分訓練集和測試集
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=5)

# 建立決策樹回歸模型
model = DecisionTreeRegressor(random_state=5)
# 擬合模型
model.fit(X_train, y_train)

# 進行預測
y_pred = model.predict(X_test)

print(f"y_test={y_test.to_numpy()}")
print(f"y_pred={y_pred}")

# R平方係數
r2 = r2_score(y_test, y_pred)
print(f"R平方係數:{r2:.3f}")

# y_test=[21376.88  2020.91  4372.62 ... 16527.55 37469.44   107.32]
# y_pred=[1.680736e+04 1.787640e+03 4.751260e+03 ... 1.441381e+04 3.348333e+04
#  2.557000e+01]
# R平方係數:0.945