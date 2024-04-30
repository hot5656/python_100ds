# 運動相簿爬取
# [運動筆記](https://running.biji.co/)
# https://running.biji.co/index.php?q=album&act=photo_list&album_id=52183&cid=11282&start=1713672000&end=1713672600&type=place&subtitle=Running%20Holidays%EF%BC%8D2024%E6%96%B0%E5%8C%97%E5%B8%82%E9%90%B5%E9%81%93%E9%A6%AC%E6%8B%89%E6%9D%BE%E6%8E%A5%E5%8A%9B%E8%B3%BD-%E8%BF%BD%E7%81%AB%E8%BB%8A%E7%AC%AC7%E6%A3%92

import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

MAX_IMAGES = 25

def main():
    # get title
    page_url = 'https://running.biji.co/index.php?q=album&act=photo_list&album_id=52183&cid=11282&start=1713672000&end=1713672600&type=place&subtitle=Running%20Holidays%EF%BC%8D2024%E6%96%B0%E5%8C%97%E5%B8%82%E9%90%B5%E9%81%93%E9%A6%AC%E6%8B%89%E6%9D%BE%E6%8E%A5%E5%8A%9B%E8%B3%BD-%E8%BF%BD%E7%81%AB%E8%BB%8A%E7%AC%AC7%E6%A3%92'
    try:
        page_resp = requests.get(page_url)
    except:
        page_resp = None

    if page_resp and page_resp.status_code == 200:
        soup = BeautifulSoup(page_resp.text, 'html.parser')
        title = soup.select('.album-title.flex-1')[0].text.strip()
        print(title)
        # create dir
        create_dir(title)

        # ajax get html
        start_row = 0
        total_images = 0
        while True:
            ajax_url = 'https://running.biji.co/index.php?pop=ajax&func=album&fename=load_more_photos_in_listing_computer'
            payload = {
                        'type': 'place',
                        'rows': str(start_row),
                        'need_rows': '20',
                        'cid': '11282',
                        'album_id': '52183'
                    }
            try:
                ajax_resp = requests.post(ajax_url, data=payload)
            except:
                ajax_resp = None
                # if not ajax error the end.
                print('if not ajax error the end.')
                break

            if ajax_resp and ajax_resp.status_code == 200:
                soup = BeautifulSoup(ajax_resp.text, 'html.parser')
                images = soup.select('.photo-img')
                # show group load
                print(payload)
                # if no image then end.
                if len(images) == 0:
                    print('if no image then end.')
                    break
                for index, image in enumerate(images):
                    # print(image.get('src'))
                    download_image(image.get('src'), title, title+str(start_row+index+1))
                total_images += len(images)

            start_row += 20
            # check maximum load images
            if start_row >= MAX_IMAGES :
                print(f'over {MAX_IMAGES} images break.')
                break
        # show total load images
        print(f"total load {total_images} images.")


def create_dir(dir_name):
    if not os.path.exists(dir_name) :
        os.makedirs(dir_name)

def detect_image_type(content):
    try:
        # Open the image from the content
        with Image.open(BytesIO(content)) as img:
        # open the image from file
        # with Image.open(file_path) as img:
            # Get the format of the image
            image_format = img.format.lower()

            # jpeg same as jpg
            if image_format == 'jpeg':
                return 'jpg'  # Return 'jpg' if the format is 'jpeg'
            else:
                return image_format
            return img.format.lower()
    except Exception as e:
        print("Error:", e)
        return None

def download_image(url, dir_name, filename):
    # get image
    try :
        resp = requests.get(url)
        if resp.status_code == 200:
            # check image type
            image_type = detect_image_type(resp.content)

            # save image
            image_name = f"{filename}.{image_type}"
            with open(os.path.join(dir_name, image_name), 'wb') as file:
                file.write(resp.content)
            print(f"download image {image_name}.")
    except:
        print(f"error download image {image_name}...")

if __name__ == '__main__':
    main()