import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
#  pip install gspread oauth2client

auto_json = './python-test2-420806-5e6b25124859.json'
# gs_scopes = ['http://spreadsheets.google.com/feeds']
# gs_scopes = ['https://www.googleapis.com/auth/spreadsheets']
# cr = sac.from_json_keyfile_name(auto_json, gs_scopes)
cr = sac.from_json_keyfile_name(auto_json, ['https://www.googleapis.com/auth/spreadsheets'])

gc = gspread.authorize(cr)

# gsheet = gc.open('PythonConnectSheet1')
# PythonConnectSheet1
gsheet = gc.open_by_key('5e6b2512485925cea5c9b714bbdd26b954790123')

wks = gsheet.sheet1
wks.clear()
list_title = ['座號','姓名','國文','英文','數學']
wks.append_row(list_title)
list_datas = [[1, '大明', 65, 62, 40],
              [2, '小華', 85, 90, 87],
              [3, '小美', 92, 90, 95]]
for list_data in list_datas:
    wks.append_row(list_data)

