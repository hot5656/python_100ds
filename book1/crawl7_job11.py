# 104 擷取職缺資料 存至 excel
import requests
from bs4 import BeautifulSoup
import  openpyxl
import os
from datetime import datetime

def main():
    page_index = 0
    index = 1
    # job_request = '前端工程師'
    job_request = '硬體研發主管'
    file_job = "job11.xlsx"
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
        job_url = f'https://www.104.com.tw/jobs/search/?ro=1&keyword={job_request}&expansionType=area,spec,com,job,wf,wktm&order=1&asc=0&page={page_index}&mode=s&jobsource=index_s&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'
        jobs = get_jobs(job_url+str(page_index))
        rows = len(jobs)
        rows_total += rows
        if len(jobs) <= 0 :
            break
        for job in jobs:
            show_job(f"({index}-{page_index},{rows})", job, sheet, sheet_temp)
            # print(f"{index}-{page_index},{rows}")
            index += 1
        print(f"page {page_index} = {rows}")
    print(f"rows_total = {rows_total}")

    # save - overwrite is ok
    workbook.save(file_job)

def show_job(head, job, sheet, sheet_temp):
    work = job.select_one(".b-tit a")
    title = work.text
    work_url =  work['href']
    comapny_name = job.select_one(".b-list-inline.b-clearfix:not(.b-content) a").text.strip()
    comapny_category = job.select(".b-list-inline.b-clearfix:not(.b-content) li")[-1].text
    work_location = job.select_one(".b-list-inline.b-clearfix.job-list-intro.b-content li").text
    try:
        default = job.select_one(".job-list-tag .b-tag--default")
        if default:
            salary = default.text
        else:
            salary = job.select_one(".job-list-tag.b-content a").text
    except:
        salary = "*****************wait check *******************"

    apply_people =  job.select_one(".b-block__right.b-pos-relative a").text.replace("人應徵", "")
    try:
        other = job.select_one(".job-list-item__info").text
    except:
        # 無列出
        other = ""

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
    # print(f"    其他事項: {other}")

def get_jobs(url):
    jobs = []

    try:
        resp = requests.get(url)
    except:
        resp = None

    if resp and resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        jobs = soup.select('article.b-block--top-bord:not(.b-block--ad)')

    return jobs

if __name__ == '__main__':
    main()