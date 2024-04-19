# 資料查詢
import sqlite3

# fetchall() 讀取所有, 無資料傳回 None
# fetchone() 讀取單筆, 無資料傳回 None

# 讀取全部
conn = sqlite3.connect('school.db')
cursor = conn.execute("SELECT * FROM scores2")
rows = cursor.fetchall()
print(rows)
for row in rows:
    print(row[0], row[1])
conn.close()
# [(1, '大熊', 65, 62, 40), (2, '小明', 85, 90, 87), (3, '小美', 92, 90, 95)]
# 1 大熊
# 2 小明
# 3 小美

# 讀取單筆
conn = sqlite3.connect('school.db')
cursor = conn.execute("SELECT * FROM scores2")
row = cursor.fetchone()
print(row[0], row[1])
conn.close()
# 1 大熊

