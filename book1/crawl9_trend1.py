# 擷取即時關鍵字及資料
# [google 搜尋趨勢](https://trends.google.com/trends)
import requests
import json

def main():

    # url = "https://trends.google.com/trends/api/dailytrends?hl=zh-TW&tz=-480&geo=TW&hl=zh-TW&ns=15"
    # 以 pamas 帶入參數
    url = "https://trends.google.com/trends/api/dailytrends"
    try:
        # resp = requests.get(url)
        # 以 pamas 帶入參數
        payload = {
            "hl": "zh-TW",
            "tz": "-480",
            "geo": "TW",
            # 加上 ed 可指定日期,否則取兩日資料
            # 但如當日,還是會取兩日資料
            # 再試時只取當日
            # "ed": "20240513",
            "ns": "15"
        }
        resp = requests.get(url, params=payload)
    except:
        resp = None

    if resp and resp.status_code == 200:
        # split_datas = resp.text.split(",", 1)
        # print(len(split_datas))
        # remove head string ")]}',"
        json_text = resp.text.replace(")]}',", "")
        try :
            # json to dict
            datas = json.loads(json_text)

            # print dict as good view
            # ensure_ascii=False show chinese correct
            # print(json.dumps(datas, indent=2, ensure_ascii=False))

            # print dict key and variable
            # for key , value in datas.items():
            #     print(f"{key}: {value}")
            #     print(f"{key}: ..")
        except json.JSONDecodeError as e:
            print("Erro decoding JSON:", e)

        for day_data in datas['default']['trendingSearchesDays']:
            show_day_trend(day_data)

def show_day_trend(day_data):
    print("日期:", day_data['formattedDate'])
    items = day_data['trendingSearches']
    for item in items:
        print(f"主題關鍵字 : {item['title']['query']}")
        for index, article in enumerate(item['articles']):
            print(f"  ({index+1}) 標    題 : {article['title']}")
            print(f"      媒    體 : {article['source']}")
            print(f"      發布時間 : {article['timeAgo']}")
            print(f"      內    容 : {article['snippet']}")
            print(f"      相關連接 : {article['url']}")

if __name__ == '__main__':
    main()

