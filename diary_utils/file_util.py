"""
透過 append_to_file() 將這句反轉文字存入 diary.txt 檔案
4.透過 print_file_info() 印出 diary.txt 所有內容
"""

def append_to_file(file_name,data):
    try:
        f = open(file_name,'a',encoding="UTF-8")
        f.write(data)
        f.write("\n")
    except Exception as e:
        print(f"寫入錯誤是: {e}")



def print_file_info(file_name):
    f = None
    """
    功能：印出指定檔案的內容
    :param file_name: 檔案路徑
    :return: None
    """
    try:
        f = open(file_name, 'r', encoding="UTF-8")
        # 讀取全部
        print("檔案讀取結果: ")
        print(f.read())
    except Exception as e:
        print(f"抓取錯誤是: {e}")
    finally:
        if f:  # 確保 f 不是 None 才調用 close()
            f.close()
