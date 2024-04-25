import gspread
from google.oauth2.service_account import Credentials

# control scope
scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

# credentials
creds = Credentials.from_service_account_file("tutorial-sheets-421106-4878ffb056ac.json", scopes=scopes)
client = gspread.authorize(creds)
# open google sheet
sheet_id = '1ToRUfJe6XIeWMu96zRMfO58kUI2Or9hkPjX1g0V27I4'
workbook = client.open_by_key(sheet_id)

values = [
    ['Name', 'Price', 'Quantity'],
    ['Baskeball', 29.00, 1],
    ['Jeans', 39.99, 4],
    ['Soap', 7.99, 3],
]

# add/clear worksheet
worksheet_list = map(lambda x: x.title, workbook.worksheets())
new_worksheet_name = 'Values'
if new_worksheet_name in worksheet_list:
    sheet = workbook.worksheet(new_worksheet_name)
else:
    sheet = workbook.add_worksheet(new_worksheet_name, rows=10, cols=10)
sheet.clear()

# update workseet by field
# for i, row in enumerate(values):
#     for j, value in enumerate(row):
#         sheet.update_cell(i + 1, j + 1, value)
# uadate worksheet by block
sheet.update(range_name=f"A1:C{len(values)}", values=values)

# add sum field
sheet.update_cell(len(values)+1, 2, f"=sum(B2:B{len(values)})")
sheet.update_cell(len(values)+1, 3, f"=sum(C2:C{len(values)})")

# change field format : 粗體字
sheet.format('A1:C1', {'textFormat': {'bold': True}})



