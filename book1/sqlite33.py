# 資料修改
import sqlite3

# 更新資料
conn = sqlite3.connect('school.db')
conn.execute("UPDATE scores2 SET name='{}' WHERE id={}".format('小王', 1))
# 更新
conn.commit()

# 刪除資料
conn.execute("DELETE FROM scores2 WHERE id={}".format(2))
# 更新
conn.commit()

# print data
rows = conn.execute("SELECT * from scores2")
for row in rows:
    print(row)

# close DB connect
conn.close()
# (1, '小王', 65, 62, 40)
# (3, '小美', 92, 90, 95)

# 刪除資料表
conn = sqlite3.connect('school.db')
conn.execute("DROP TABLE scores2")
# 更新
conn.commit()
# close DB connect
conn.close()

# show table
conn = sqlite3.connect('school.db')
# cursor = conn.cursor()
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
# tables = cursor.fetchall()
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
print('-- tables --')
for table in tables:
    print(table)
# close DB connect
conn.close()
# -- tables --
