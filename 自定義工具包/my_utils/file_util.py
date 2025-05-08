"""
文件處理相關工具
- 函數: print_file_info(file_name),接收傳入文件路徑,打印文件的全部內容,如文件不存在則捕獲異常,輸出提示信息,通過finally關閉文件對象
- 函數: append_to_file(file_name,data),接收文件路徑以及傳入數據,將數據追加寫入文件中
"""
def print_file_info(file_name):
    f = None  # 一開始先設為 None
    """
    功能是: 將給定路徑的文件內容輸出到控制台中
    :param file_name: 即將讀取的文件路徑
    :return: None
    """
    try:
        f = open(file_name, "r",encoding="UTF-8")
        read = f.read()
        print("讀取檔案為: ")
        print(read)
    except Exception as e:
        print(f"抓到錯誤了: {e}")
    finally:
        if f:
            f.close()
"""
抓到錯誤了: [Errno 2] No such file or directory: 'C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/test_write.ttxt'
讀取檔案為: 
ha ha changed!
Hello World is back!!

"""

#
def append_to_file(file_name,data):
    """
    功能 : 將指定數據加入指定文件中
    :param file_name:  指定檔案
    :param data: 指定數據
    :return: None
    """
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()
if __name__ == '__main__':
    print_file_info("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/test_write.ttxt")
    print_file_info("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/test_write.txt")
    print(append_to_file("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/test_write.txt","yaha"))
