# Automate Google Sheets With Python - Google Sheets API Tutorial
# https://www.youtube.com/watch?v=zCEJurLGFRk
# gspread document
# https://docs.gspread.org/en/latest/user-guide.html#opening-a-spreadsheet
# create virtual python
# python -m venv sheets
# install package
# pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib gspread


import gspread
from google.oauth2.service_account import Credentials

# control scope
scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

# credentials & id
creds = Credentials.from_service_account_file("tutorial-sheets-421106-4878ffb056ac.json", scopes=scopes)
client = gspread.authorize(creds)
sheet_id = '1ToRUfJe6XIeWMu96zRMfO58kUI2Or9hkPjX1g0V27I4'

# show 1st row
# sheet = client.open_by_key(sheet_id)
# values_list = sheet.sheet1.row_values(1)
# print(values_list)
#
# python .\google-sheet2.py
# ['test value']
# add value2
# python .\google-sheet2.py
# ['test value', 'value2']

workbook = client.open_by_key(sheet_id)
# get worksheets
# sheets = workbook.worksheets()
# print(sheets)
#
# [<Worksheet 'sheet_1st' id:0>, <Worksheet '工作表2' id:197625105>]
# get worksheets by list
sheets = map(lambda a: a.title, workbook.worksheets())
print(list(sheets))
#
# ['sheet_1st', '工作表2']

# update worksheel title
# sheet = workbook.worksheet('sheet_1st')
# sheet.update_title('Hello World')

# update filed
sheet = workbook.worksheet('Hello World')
# sheet.update_cell(1,1, 'HELLO WORLD THIS IS CHANGED')
# sheet.update_acell('A1', 'HELLO WORLD THIS IS CHANGED')

# get filed
# value = sheet.acell('A1').value
# print(value)

# find filed
cell = sheet.find('tim is great')
print(cell, cell.row, cell.col)
# <Cell R2C3 'tim is great'> 2 3

# change field format : 粗體字
sheet.format('A1:B2', {'textFormat': {'bold': True}})