# Line Notify 通知
# [Line Notify](https://notify-bot.line.me/zh_TW/)
# window set/show evn by cmd
# set LINE_NOTIFY_TOKEN=string
# echo %LINE_NOTIFY_TOKEN%
# window set/show evn by powershell
# $env:LINE_NOTIFY_TOKEN = "...."
# $env:LINE_NOTIFY_TOKEN


import requests
import os

notify_url = "https://notify-api.line.me/api/notify"
msg = "get token by windows env..2"
token = os.getenv("LINE_NOTIFY_TOKEN")

headers = {
    "Authorization": "Bearer " + token,
    "Connect-Type" : "application/x-www-form-urlencoded"
}
payload = {"message": msg}

notify = requests.post(notify_url,
                headers = headers,
                params = payload)
if notify.status_code == 200:
    print("Send LINE Notify success!")
else:
    print("Send LINE Notify fail!")
