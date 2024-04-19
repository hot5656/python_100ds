# json
import json
# json.load(file) : load json file
# json.loads(string) : load for json string
# json.dump('filename', file) : save to json file
# json.dumps(string) : save json string

# json load string
class_str = """
{
    "class A" : [
        {
            "id": 1,
            "name": "小美",
            "Math": 65,
            "Chinese": 62,
            "English": 30

        },
        {
            "id": 2,
            "name": "王大明",
            "Math": 65,
            "Chinese": 62,
            "English": 30

        },
        {
            "id": 3,
            "name": "Bill",
            "Math": 92,
            "Chinese": 90,
            "English": 85
        }
    ]
}
"""
datas = json.loads(class_str)
print('-- json from string --')
print(type(datas))
for data in datas['class A']:
    print(data)
# <class 'dict'>
# {'id': 1, 'name': '小美', 'Math': 65, 'Chinese': 62, 'English': 30}
# {'id': 2, 'name': '王大明', 'Math': 65, 'Chinese': 62, 'English': 30}
# {'id': 3, 'name': 'Bill', 'Math': 92, 'Chinese': 90, 'English': 85}

# save to json file
with open('class_a_1.json', 'w', encoding='utf-8') as f:
    # ensure_ascii=False 顯示正確中文
    json.dump(datas, f, ensure_ascii=False )

# load json from file
with open('class_a_1.json', 'r', encoding='utf-8') as f:
    datas2 = json.load(f)
print('-- json from file --')
print(type(datas2))
for data in datas2['class A']:
    print(data)
# <class 'dict'>
# {'id': 1, 'name': '小美', 'Math': 65, 'Chinese': 62, 'English': 30}
# {'id': 2, 'name': '王大明', 'Math': 65, 'Chinese': 62, 'English': 30}
# {'id': 3, 'name': 'Bill', 'Math': 92, 'Chinese': 90, 'English': 85}

# save to jason string
class_str2 = json.dumps(datas2, ensure_ascii=False)
print('-- json to string --')
print(type(class_str2))
print(class_str2)
# <class 'str'>
# {"class A": [{"id": 1, "name": "小美", "Math": 65, "Chinese": 62, "English": 30}, {"id": 2, "name": "王大明", "Math": 65, "Chinese": 62, "English": 30}, {"id": 3, "name": "Bill", "Math": 92, "Chinese": 90,
# "English": 85}]}