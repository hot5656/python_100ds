# validate.py
import re

# .: any character except a newline
# *: 0 or more repetitions
# +: 1 or more repetitions
# ?: 0 or 1 repetition
# {m}: m repetitions,o{2} 含 "oo"
# {m,n}: m-n repetitions
# ^: matches the start of the string
#    ^插入符號是比對前開頭,比如你輸入的搜尋條件是  ^eat，那麼你會搜尋到的結果會有 eat、eaten
# $: matchs the end or the string just before the newline at the end of the string
#    $ 錢字符號則是比對結尾,如果是 eat$，那麽搜尋到的結果可能是 creat、peat、leat
# []: set of characters(包含)
# [^]: complementing the set(不包含)
# \w: [a-zA-Z0-9_]
# \W: [^a-zA-Z0-9_]
# \d: [0-9]
# \D: [^0-9]
# \s: [ \r\t\n\f]
# \S: [^ \r\t\n\f]
# A|B: either A or B
# (...) : group
# (?:...): non-capturing version

# re.IGNORECASE : ignore case
# re.MULTILINE: multiple line
# re.DOTALL


# re.search(pattern, string, flags=0)
email = input("What's your email? ").strip()
# if re.search(r"^[^@ ]+@[^@]+\.(edu|com|gov|net|org)$", email):
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")