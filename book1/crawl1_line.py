import requests
from bs4 import BeautifulSoup
import json
import imghdr
import os

TARGET_URL = 'https://store.line.me/stickershop/product/30858/zh-Hant'
FILE_PREFIX = 'mouse'
FOLDER = FILE_PREFIX

def main():
    try:
        resp = requests.get(TARGET_URL)
    except:
        resp = None

    if resp and resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        # UnicodeEncodeError: 'cp950' codec can't encode character '\u2661' in position 7107: illegal multibyte sequence
        # print(soup.encode('utf-8'))
        # print(type(soup))
        try :
            # select by class
            datas = soup.select('.FnStickerList .FnStickerPreviewItem')

            # create folder
            if not os.path.exists(FOLDER) :
                os.makedirs(FOLDER)

            for index, data in enumerate(datas):
                # get data_preview from json
                data_preview = json.loads(data['data-preview'])
                # down load image
                download_image(data_preview['fallbackStaticUrl'], FILE_PREFIX+str(index+1))
        except :
            print('No any figure...')

def download_image(url, filename):
    # get image
    resp = requests.get(url)
    if resp.status_code == 200:
        # check image type
        image_type = imghdr.what(None, resp.content)
        # save image
        image_name = f"{filename}.{image_type}"
        with open(os.path.join(FOLDER, image_name), 'wb') as file:
            file.write(resp.content)
        print(f"download image {image_name}.")
    else:
        print("Failed to download from '{url}'")

if __name__ == '__main__':
    main()