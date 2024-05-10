# 擷取職缺資料 存至 excel
import requests
from bs4 import BeautifulSoup
import  openpyxl
import os
from datetime import datetime

job_no = 0
def main():
    global job_no

    page_index = 0
    index = 1
    job = '前端工程師'
    # job = '硬體工程師'
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")

    job_url = f'https://www.1111.com.tw/search/job?col=wc&ks={job}&tt=1&page='

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
    sheet.title = f"1111 {date_string} {job}"
    sheet_temp = workbook_temp.worksheets[0]
    # 新增一列
    sheet.append(list_titles)

    # show 1st page and title
    page_index += 1
    jobs = get_jobs(job_url+str(page_index), index)
    print(f"-- job_no = {job_no} --")
    rows = len(jobs)
    for job in jobs:
        show_job(f"({index}-{page_index},{rows})", job, sheet, sheet_temp)
        index += 1

    # show other pages
    while index <= job_no:
        page_index += 1
        jobs = get_jobs(job_url+str(page_index), index)
        rows = len(jobs)
        # if no more data break
        if rows == 0:
            break

        for job in jobs:
            show_job(f"({index}-{page_index},{rows})", job, sheet, sheet_temp)
            index += 1
            if (index > job_no):
                break

    file_job = "job1.xlsx"
    # if os.path.exists(file_job):
    #     os.remove(file_job)

    # save - overwrite is ok
    workbook.save(file_job)

def show_job(head, job, sheet, sheet_temp):
    work = job.select_one(".title a")
    title = work.text
    work_url =  "https://www.1111.com.tw" + work['href']
    comapny = job.select_one(".company a").text.split('|')
    comapny_name = comapny[0]
    comapny_category = comapny[1].strip()
    work_location = job.select_one(".other a")['data-after']
    salary = job.select_one(".other span")['data-after']
    apply_people =  job.select_one(".people p").text.replace("應徵人數｜", "").replace(" 人", "")
    other = job.select_one(".introduce").text

    # check error
    try:
        sheet_temp.append([other])
    except:
        # print(f"{head} {title}")
        # print("=============")
        # print(other)
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
        sheet.append(datas)
    except :
        print("=============")
        print(datas)

    # # 職務名稱
    # print(f"{head} {title}")
    # print(f"    工作網址: {work_url}")
    # print(f"    公司名稱: {comapny_name}")
    # print(f"    公司類別: {comapny_category}")
    # print(f"    工作地點: {work_location}")
    # print(f"    薪資:     {salary}")
    # print(f"    應徵人數: {apply_people}")
    # # print(f"    其他事項: {other}")

def get_jobs(url, index):
    global job_no

    try:
        resp = requests.get(url)
    except:
        resp = None

    if resp and resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")

        # count job number
        if job_no == 0:
            try:
                job_no = int(soup.select_one(".top .left span").text)
            except:
                job_no = 0

        try:
            # jobs = soup.select(".item__job .title a")
            jobs = soup.select(".item__job")
        except:
             jobs = []

        return jobs

if __name__ == '__main__':
    main()