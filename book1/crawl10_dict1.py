# (萌點)[https://www.moedict.tw/]
import requests
import json

word = '行'
url = f"https://www.moedict.tw/uni/{word}"
resp = requests.get(url)
if resp and resp.status_code == 200:
    info = json.loads(resp.text)
    # print(json.dumps(info, indent=2, ensure_ascii=False))

    print(f"查詢字詞:{info['title']}")
    print(f"部首:{info['radical']}")
    print(f"筆畫:{info['stroke_count']}")
    # print(len(info['heteronyms']))
    for index, data in enumerate(info['heteronyms']):
        print(f"[{index+1}]")
        print(f"  注音:{data['bopomofo']}")
        print(f"  羅馬拼音:{data['bopomofo2']}")
        print(f"  漢語拼音:{data['pinyin']}")
        for i, item in enumerate(data['definitions']):
            print(f"  ({i+1}):{item['def']}")
            if "type" in item:
                print(f"    詞性：{item['type']}")
            if "example" in item:
                print(f"    解釋：{item['example']}")
            if "quote" in item:
                print(f"    引用：{item['quote']}")
            if "link" in item:
                print(f"    參考")
                for ref in item['link']:
                     print(f"      {ref}")

