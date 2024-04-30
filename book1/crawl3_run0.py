# URL unicode 轉成中文
# pip install googletrans==4.0.0-rc1
from googletrans import Translator
import urllib.parse
def main():
    url = "https://running.biji.co/index.php?q=album&act=photo_list&album_id=52183&cid=11282&start=1713672000&end=1713672600&type=place&subtitle=Running%20Holidays%EF%BC%8D2024%E6%96%B0%E5%8C%97%E5%B8%82%E9%90%B5%E9%81%93%E9%A6%AC%E6%8B%89%E6%9D%BE%E6%8E%A5%E5%8A%9B%E8%B3%BD-%E8%BF%BD%E7%81%AB%E8%BB%8A%E7%AC%AC7%E6%A3%92"
    translated_url = translate_url(url)
    print(translated_url)

def translate_url(url):
    translator = Translator()
    translated_url = translator.translate(urllib.parse.unquote(url), dest='zh-TW').text
    return translated_url

if __name__ == '__main__':
    main()

# https://running.biji.co/index.php?q=album&act=photo_list&album_id=52183&cid=11282&start=1713672000&end=1713672600&type=place&subtitle=Running Holidays－2024新北市鐵道馬拉松接力
# 賽-追火車第7棒