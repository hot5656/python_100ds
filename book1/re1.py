import re
# match(string) : 傳回符合字串object,不符合傳回Nonw
# search(string) : 傳回第一組符合字串,不符合傳回Nonw
# findall(string) : 傳回所有符合字串 by [],不符合傳回Nonw,無符合傳回空串列

# === match(string) ===
# 傳回物件
# group():傳回符合表達式字串
# start():傳回match開始位置
# end():傳回match結束位置
# span():傳回 match (開始位置,結束位置)
m = re.match(r'[a-z]+','abc123xyz')
print(m)
if m != None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
# <re.Match object; span=(0, 3), match='abc'>
# abc
# 0
# 3
# (0, 3)
m = re.match(r'[a-z]+','123')
print(m)
# None

# search(string)
m = re.search(r'[a-z]+','abc123xyz')
print("-- search --")
print(m)
if m != None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())

# findall(string)
m = re.findall(r'[a-z]+','abc123xyz')
print("-- findall --")
print(m)
# ['abc', 'xyz']

# 正規表達式取代內容
# re.sub(正規表達式,取代字串,搜尋字串,count=0)
# count 表取代次數, 0 表全部取代
result = re.sub("\d+", "*", "Password:1234, ID=5678")
print(result)
result = re.sub("\d+", "*", "Password:1234, ID=5678",count=1)
print(result)
# Password:*, ID=*
# Password:*, ID=5678