# 新書排行榜資料 存至 google sheet
# [Google Sheets 指南](https://developers.google.com/sheets/api/guides/filters?hl=zh-tw)
import gspread
from google.oauth2.service_account import Credentials

import requests
from bs4 import BeautifulSoup
import time

NEW_BOOK_URL = "https://www.books.com.tw/web/books_newbook/"
book_list_get = []
def main():
    # save_to_google_sheet()
    # return

    book_list = book_types(NEW_BOOK_URL)
    for index,item in enumerate(book_list):
        print(f"({index+1}) {item['title']}")
        # get_books(index+1, item['url'], item['title'])
        # time.sleep(1)
    # get select book type
    kind_no = int(input("輸入圖書分類:"))
    if kind_no >= 1 and kind_no <= len(book_list):
        get_books(kind_no, book_list[kind_no-1]['url'], book_list[kind_no-1]['title'])
        # save to google sheet
        save_to_google_sheet()
        # for book in book_list_get:
        #     print(book)
    else:
        print("分類錯誤!")

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
        books_no = show_books(title, start_index, soup)
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
                books_no = show_books(title, start_index, soup)
                start_index += books_no

def show_books(type_title, start_index, soup):
    global book_list_get

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

        # print(f"    ({index+start_index}) {title}")
        # print(f"         圖片網址:{img_url}")
        # print(f"         作者:{author}")
        # print(f"         出版社:{publisher}")
        # print(f"         出版日期:{publish_date}")
        # if (special_discount != '100'):
        #     print(f"         折扣:{special_discount}折")
        # print(f"         優惠價:{special_price}元")
        # print(f"         內容:{content}")
        list_data = [type_title, title, img_url, author, publisher, publish_date, special_discount, special_price, content]
        book_list_get.append(list_data)
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
                        'url': type['href'].split("?")[0]
                    }
                )
        return book_list

def save_to_google_sheet():
    global book_list_get

    # control scope
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets"
    ]

    # credentials & id
    creds = Credentials.from_service_account_file("tutorial-sheets-421106-4878ffb056ac.json", scopes=scopes)
    client = gspread.authorize(creds)
    sheet_id = '1m6s3HXmc6vtVuvbgF5MytNIGB1BgdnovDWdqT7pJZJs'

    workbook = client.open_by_key(sheet_id)
    # # get worksheets by list
    # sheets = map(lambda a: a.title, workbook.worksheets())
    # print(list(sheets))

    # # get worksheets
    # sheets = workbook.worksheets()
    # print(sheets)
    # # update 1 field
    # sheets[0].update_acell('A1', "Hello")

    # 清出工作表
    # get active sheet
    print("save books to google sheet..")
    sheet = workbook.get_worksheet(0)
    sheet.clear()
    list_title = ["分類", "書名", "圖片網址", "作者", "出版社", "出版日期", "折扣", "優惠價", "內容"]
    sheet.append_row(list_title)
    for item in book_list_get:
        sheet.append_row(item)
        time.sleep(1.2) # delay 太短會中斷


if __name__ == '__main__':
    main()