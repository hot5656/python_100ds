# 新增資料表,資料
import sqlite3
import os

# if file exist, delete it
SCHOOL_DB_FILE = 'school.db'
if os.path.isfile(SCHOOL_DB_FILE):
    os.remove(SCHOOL_DB_FILE)

# 新增資料表
# 常用類型
# INTERGER 整數,大小有 1,2,3,4,6,8 bytes
# REAL float 8 byted
# TEXT 不定長度字串 format UTF-8/UTF-16BE/UTF16LE
# BLOB true/false
conn = sqlite3.connect(SCHOOL_DB_FILE)
sql_str = '''CREATE TABLE IF NOT EXISTS scores2
("id" INTEGER PRIMARY KEY NOT NULL,
 "name" TEXT NOT NULL,
 "chinese" INTEGER NOT NULL,
 "english" INTEGER NOT NULL,
 "math" INTEGER NOT NULL
)
'''
conn.execute(sql_str)
# 更新
conn.commit()
# close DB connect
conn.close()

# 新增資料表
conn = sqlite3.connect(SCHOOL_DB_FILE)
datas = [[1, '大熊', 65, 62, 40],
         [2, '小明', 85, 90, 87],
         [3, '小美', 92, 90, 95]]
for data in datas:
    conn.execute("INSERT INTO scores2 (id, name, chinese, english, \
        math) VALUES ({}, '{}', {}, {}, {})".format(data[0],\
        data[1], data[2], data[3], data[4]))
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

# ('scores2',)



