# pip3 install pypdf
# pip3 install cryptography --upgrade
# from pypdf import PdfReader

# reader = PdfReader('example.pdf')

# print(f'pages = {len(reader.pages)}')
# page = reader.pages[0]

# text = page.extract_text()
# print(text)


# from pypdf import PdfReader

# # 從使用者輸入 PDF 檔案名稱和頁數
# pdf_file = input("請輸入 PDF 檔案名稱: ")
# page_num = int(input("請輸入要提取的頁數 (從 1 開始): "))

# # 讀取 PDF
# reader = PdfReader(pdf_file)

# # 確認頁數是否有效
# if page_num > len(reader.pages) or page_num < 1:
#     print("頁數無效，超出範圍")
# else:
#     # 提取指定頁面的文字
#     page = reader.pages[page_num - 1]
#     text = page.extract_text()

#     # 分割每一行文字
#     lines = text.split('\n')

#     # 將結果保存到文字檔案，但排除包含條件
#     output_file = "output.txt"
#     with open(output_file, "w", encoding="utf-8") as f:
#         for line in lines:
#             if "Confidential for" not in line and "tony.yang" not in line:
#                 f.write(line + '\n')
#         # f.write(text)

#     print(f"已提取第 {page_num} 頁內容並保存到 {output_file} 檔案中。")

import sys
from pypdf import PdfReader

def extract_pdf_text(pdf_file, page_num, exclusion_keywords):
    # 讀取 PDF
    reader = PdfReader(pdf_file)

    # 確認頁數是否有效
    if page_num > len(reader.pages) or page_num < 1:
        print("頁數無效，超出範圍")
        return

    # 提取指定頁面的文字
    page = reader.pages[page_num - 1]
    text = page.extract_text()

    # 分割每一行文字
    lines = text.split('\n')

    # 動態生成輸出檔案名稱，例如 output_1.txt
    output_file = f"output_{page_num}.txt"

    # 將結果保存到文字檔案，但排除包含任何條件字串的行
    with open(output_file, "w", encoding="utf-8") as f:
        for line in lines:
            # 檢查是否包含任何要排除的字串
            if not any(keyword in line for keyword in exclusion_keywords):
                f.write(line + '\n')

    print(f"已提取第 {page_num} 頁內容並保存到 {output_file} 檔案中。")


if __name__ == "__main__":
    # 檢查是否有足夠的命令列參數
    if len(sys.argv) != 3:
        print("用法: python pdf_to_text.py <pdf檔案> <頁數>")
        sys.exit(1)

    # 從命令列參數取得 PDF 檔案名稱和頁數
    pdf_file = sys.argv[1]
    page_num = int(sys.argv[2])

    # 在程式內部設定要排除的字串陣列
    exclusion_keywords = ["Confidential for", "tony.yang", "private", "restricted"]

    # 執行提取函數
    extract_pdf_text(pdf_file, page_num, exclusion_keywords)
