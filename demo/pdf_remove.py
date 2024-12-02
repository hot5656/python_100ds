# pip3 install pikepdf
import sys
import os
import pikepdf

# def remove_password_from_pdf(filename, password=None):
#     pdf = pikepdf.open(filename, password=password)
#     pdf.save("new.pdf")

def remove_password_from_pdf(filename, password=""):
    try:
        # Open the PDF file with the provided password
        pdf = pikepdf.open(filename, password=password)
        new_name = os.path.splitext(filename)[0] + "_1" + ".pdf"
        # Save the PDF without a password
        pdf.save(new_name)
        print(f"Saved as {new_name}.")
    except pikepdf._qpdf.PasswordError:
        print("Failed to open the PDF. Incorrect or missing password.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 檢查是否有足夠的命令列參數
    # print(f"parameter len =${len(sys.argv)}")
    if len(sys.argv) < 2:
        print("用法: python pdf_remove.py <pdf檔案> ")
        sys.exit(1)
    else:
        # 從命令列參數取得 PDF 檔案名稱和頁數
        pdf_file = sys.argv[1]
        print(f"pdf_file={pdf_file}")
        if os.path.exists(pdf_file):
            remove_password_from_pdf(pdf_file)
        else:
            print(f"file {pdf_file} doesn't exist.")
