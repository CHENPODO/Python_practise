"""
diary_utils
題目說明：
請建立一個主程式 main.py，使用你自己的 str_util 和 file_util 模組，完成以下功能流程：

功能要求：
1.使用者輸入一句話（例如：我今天吃了火鍋）
2.利用 str_reverse() 把這句話反轉
3.透過 append_to_file() 將這句反轉文字存入 diary.txt 檔案
4.透過 print_file_info() 印出 diary.txt 所有內容
5.印出該句話中某個指定字元的出現次數（用 count_char()）

使用函數：
str_util.str_reverse()
str_util.count_char()

file_util.append_to_file()
file_util.print_file_info()
"""
from diary_utils import str_utli
from diary_utils import file_util

# 使用者輸入
text = input("輸入一句話")

# 反轉
reversed_text = str_utli.str_reverse(text)
print(f"反轉結果：{reversed_text}")

# 寫入檔案
file_path ="C:/Users/cindy/OneDrive/桌面/Python_practise/diary_utils"
file_util.append_to_file(file_path,reversed_text)

# 印出檔案內容
file_util.print_file_info(file_path)

# 查詢字元出現次數
char = input("請輸入要查詢的字元：")
print(f"字元「{char}」在原句中出現 {str_utli.count_char(text, char)} 次")