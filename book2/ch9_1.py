# 集合 set()
# 集合資料不重複
# 執行set(), 會刪除重複,但順序可能會被打亂
lang = {"Python", "C", "Java"}
A = set("Deepmind")
print(type(lang), lang)
print(type(A), A)
# <class 'set'> {'Python', 'C', 'Java'}
# <class 'set'> {'d', 'i', 'p', 'D', 'm', 'e', 'n'}

# 空集合要用 set()
empty_dict = {}
empty_set = set()
print(type(empty_dict))
print(type(empty_set))
# <class 'dict'>
# <class 'set'>

# 轉成 set() 刪除重複資料
fruits1 = ["apple", "orange", "banana", "apple", "orange"]
x = set(fruits1)
fruits2 = list(x)
print(fruits2)
# ['orange', 'apple', 'banana']


# set() add, remove
data_list = ['Python', 'Java', 'English']
languages = set()
for item in data_list:
    languages.add(item)
print(type(languages), languages)
# remove English from the set
languages.remove('English')
print(type(languages), languages)
# <class 'set'> {'Python', 'Java', 'English'}
# <class 'set'> {'Python', 'Java'}

