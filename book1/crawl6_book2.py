# 取得新書排行榜資料
# [博客來](https://www.books.com.tw/)
# [博客來 新書](https://www.books.com.tw/web/books_newbook/)
# [博客來 新書#2商業理財 暢銷度排序](https://www.books.com.tw/web/books_nbtopm_02/?o=5&v=1)
# [博客來 新書#2商業理財 暢銷度排序 page2](https://www.books.com.tw/web/books_nbtopm_02/?o=5&v=1&page=2)
# [博客來 新書#19電腦資訊 暢銷度排序](https://www.books.com.tw/web/books_nbtopm_02/?o=5&v=1)
# 中文書分類 ".mod_b li a"
# 新書數量 ".mod.type02_m019 .mod_a em"
# 本頁新書 ".wrap .item .msg h4 a"
# 下一頁 ".cnt_page .nxt"
# 頁數 ".cnt_page .page span" 1st

import requests
from bs4 import BeautifulSoup
import time

NEW_BOOK_URL = "https://www.books.com.tw/web/books_newbook/"
def main():
    book_list = book_types(NEW_BOOK_URL)
    for index,item in enumerate(book_list):
        print(f"({index+1}) {item['title']}")
        # get_books(index+1, item['url'], item['title'])
        # time.sleep(1)
    # get select book type
    kind_no = int(input("輸入圖書分類:"))
    if kind_no >= 1 and kind_no <= len(book_list):
        get_books(kind_no, book_list[kind_no-1]['url'], book_list[kind_no-1]['title'])

def get_books(index, url, title):
    print(f"-- {index} {title} {url} --")
    book_url = f"{url}?o=5&v=1"
    try:
        resp = requests.get(book_url)
    except:
        resp = None

    pages = 0
    start_index = 1
    if resp and resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        try:
            pages = int(soup.select_one(".cnt_page .page span").text)
        except:
            pages = 1
        books_no = show_books(start_index, soup)
        start_index += books_no

    if (pages > 1):
        for i in range(2, pages + 1):
            # print(f"i={i}..")
            book_url = f"{url}?o=5&v=1&page={str(i)}"
            try:
                resp = requests.get(book_url)
            except:
                resp = None
            if resp and resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                books_no = show_books(start_index, soup)
                start_index += books_no

def show_books(start_index, soup):
    books = soup.select(".wrap .item")
    for index,book in enumerate(books):
        title = book.select_one(".msg h4 a").text
        img_url = book.select_one(".cover")['src']
        info = book.select_one(".info").text.split('，')
        author = info[0]
        publisher = info[1]
        publish_date = info[2].split("：")[1]
        price_box = book.select(".price strong")
        if len(price_box) == 1:
            special_discount = '100'
            special_price = price_box[0].text
        else:
            special_discount = price_box[0].text
            special_price = price_box[1].text

        content = book.select_one(".txt_cont").text.strip().replace("\n", "").replace(" ", "")

        print(f"    ({index+start_index}) {title}")
        print(f"         圖片網址:{img_url}")
        print(f"         作者:{author}")
        print(f"         出版社:{publisher}")
        print(f"         出版日期:{publish_date}")
        if (special_discount != 100):
            print(f"         折扣:{special_discount}折")

        print(f"         優惠價:{special_price}元")
        print(f"         內容:{content}")
    return len(books)

def book_types(book_url):
    book_list = []
    try :
        resp = requests.get(book_url)
    except:
        resp = None

    if resp and resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")

        types = soup.select(".mod_b li a")
        for type in types:
            book_list.append(
                    {
                        'title': type.text,
                        # 'url': type['href']
                        'url': type['href'].split("?")[0]
                    }
                )
        return book_list

if __name__ == '__main__':
    main()
