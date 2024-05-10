# CakeResume 擷取職缺資料 存至 excel
# https://www.cakeresume.com/jobs/硬體研發工程師?job_type[0]=full_time&page=2
import requests
from bs4 import BeautifulSoup
import  openpyxl
import os
from datetime import datetime

def main():
    page_index = 0
    index = 1
    # job_request = '前端工程師'
    job_request = '硬體研發工程師'
    file_job = "job21.xlsx"
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")

    list_titles =["職務名稱",
            "工作網址",
            "公司名稱",
            "公司類別",
            "工作地點",
            "薪資",
            "應徵人數",
            "其他事項"]
    # 新增 excell
    # 活頁簿
    workbook = openpyxl.Workbook()
    workbook_temp = openpyxl.Workbook()
    # 工作表 #1
    sheet = workbook.worksheets[0]
    sheet.title = f"104 {date_string} {job_request}"
    sheet_temp = workbook_temp.worksheets[0]
    # 新增一列
    sheet.append(list_titles)

    rows_total = 0
    while True:
        page_index += 1
        job_url = f'https://www.cakeresume.com/jobs/{job_request}?job_type[0]=full_time&page={page_index}'
        jobs = get_jobs(job_url)
        rows = len(jobs)
        rows_total += rows
        if len(jobs) <= 0 :
            break
        for job in jobs:
            show_job(f"({index}-{page_index},{rows})", job, sheet, sheet_temp)
            # print(f"{index}-{page_index},{rows}")
            index += 1
        print(f"page {page_index} = {rows}")
        # break
    print(f"rows_total = {rows_total}")

    # save - overwrite is ok
    workbook.save(file_job)

def show_job(head, job, sheet, sheet_temp):
    work = job.select_one(".JobSearchItem_jobTitle__bu6yO")

    title = work.text
    work_url =  'https://www.cakeresume.com'+work['href']
    comapny_name = job.select_one(".JobSearchItem_companyName__bY7JI").text
    comapny_category = ""
    infomation = job.select(".JobSearchItem_features__hR3pk .InlineMessage_label__LJGjW")
    work_location = infomation[1].text

    if "TWD" in infomation[1].text:
        # 少填位置
        work_location = "-- space --"
        salary = infomation[1].text
    else:
        salary = infomation[2].text

    apply_people =  infomation[0].text.split("・")[0]
    other = job.select_one(".JobSearchItem_description__si5zg").text

    # check error
    try:
        sheet_temp.append([other])
    except:
        other="--wait--"

    datas = [
        title,
        work_url,
        comapny_name,
        comapny_category,
        work_location,
        salary,
        apply_people,
        other
    ]
    try :
        # 若非 TWD 不計入
        if "TWD" in salary:
            sheet.append(datas)
    except :
        print("=============")
        # print(f"{head} {title}")
        print(datas)

    # # 職務名稱
    # print(f"{head} {title}")
    # print(f"    工作網址: {work_url}")
    # print(f"    公司名稱: {comapny_name}")
    # print(f"    公司類別: {comapny_category}")
    # print(f"    工作地點: {work_location}")
    # print(f"    薪資:     {salary}")
    # print(f"    應徵人數: {apply_people}")
    # print(f"    其他事項: {other}")

def get_jobs(url):
    jobs = []

    try:
        resp = requests.get(url)
    except:
        resp = None

    if resp and resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        jobs = soup.select('.JobSearchItem_content__JriB9')

    return jobs

if __name__ == '__main__':
    main()