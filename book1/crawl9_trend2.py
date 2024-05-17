# 即時關鍵字及資料存檔
# [google 搜尋趨勢](https://trends.google.com/trends)
import requests
import json

def main():
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
        json_text = resp.text.replace(")]}',", "")
        try :
            # json to dict
            datas = json.loads(json_text)
        except json.JSONDecodeError as e:
            print("Erro decoding JSON:", e)

        print(len(datas['default']['trendingSearchesDays']))
        for day_data in datas['default']['trendingSearchesDays']:
            show_day_trend(day_data)

def show_day_trend(day_data):
    day_news = ""
    day_news += f"日期 : {day_data['formattedDate']}\n"
    items = day_data['trendingSearches']
    for item in items:
        day_news += f"主題關鍵字 : {item['title']['query']}\n"
        for index, article in enumerate(item['articles']):
            day_news += f"  ({index+1}) 標    題 : {article['title']}\n"
            day_news += f"      媒    體 : {article['source']}\n"
            day_news += f"      發布時間 : {article['timeAgo']}\n"
            day_news += f"      內    容 : {article['snippet']}\n"
            day_news += f"      相關連接 : {article['url']}\n"
    file_name = f"{day_data['date']}.txt"
    with open(file_name, "w", encoding="UTF-8") as f:
        f.write(day_news)
    print(f"create file {file_name}")

if __name__ == '__main__':
    main()