# [博客來](https://www.books.com.tw/)
# [博客來 新書](https://www.books.com.tw/web/books_newbook/)
# [博客來 新書#2商業理財 暢銷度排序](https://www.books.com.tw/web/books_nbtopm_02/?o=5&v=2)
# [博客來 新書#2商業理財 暢銷度排序 page2](https://www.books.com.tw/web/books_nbtopm_02/?o=5&v=2&page=2)
# [博客來 新書#19電腦資訊 暢銷度排序](https://www.books.com.tw/web/books_nbtopm_02/?o=5&v=2)
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
    kind_no = int(input("輸入圖書分類:"))
    if kind_no >= 1 and kind_no <= len(book_list):
        get_books(kind_no, book_list[kind_no-1]['url'], book_list[kind_no-1]['title'])

def get_books(index, url, title):
    print(f"-- {index} {title} {url} --")
    book_url = f"{url}?o=5&v=2"
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
        print(f"pages={pages}")
        books_no = show_books(start_index, soup)
        start_index += books_no

    if (pages > 1):
        for i in range(2, pages + 1):
            # print(f"i={i}..")
            book_url = f"{url}?o=5&v=2&page={str(1)}"
            try:
                resp = requests.get(book_url)
            except:
                resp = None
            if resp and resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                books_no = show_books(start_index, soup)
                start_index += books_no

def show_books(start_index, soup):
    books = soup.select(".wrap .item .msg h4 a")
    for index,book in enumerate(books):
        print(f"    ({index+start_index}) {book.text}")
        print(f"         {book['href']}")
    return len(books)

# def show_books_detail(book_url) :
#     try:
#         resp = requests.get(book_url)
#     except:
#         resp = None

#     if resp and resp.status_code == 200:
#         soup = BeautifulSoup(resp.text, "html.parser")
#         img_url = soup.select_one(".cnt_mod002 .cover")['src']
#         author = soup.select_one("")
#         publisher = soup.select_one("")
#         price = soup.select_one("")
#         coupon = soup.select_one("")
#         publish_date= soup.select_one("")
#         coupon_date = soup.select_one("")
#         content = soup.select_one("")




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
                        'url': type['href'].split("?")[0]
                    }
                )
        return book_list

if __name__ == '__main__':
    main()
