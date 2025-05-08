"""
函數
str_reverse()
count_char()
"""

# 字串反轉函
def str_reverse(s):
    """
    功能: 將傳入的字串 s 反轉並返回
    :param s: 要反轉的字串
    :return: 反轉後的字串
    """
    return s[::-1] # start:end:step 使用切片反轉字串

# 計算字元出現次數
def count_char(s,char):
    """
    功能:計算字串 s 中某個字元 char 出現的次數
    :param s: 查詢的字串
    :param char: 計算的字元
    :return:字元出現的次數
    """
    return s.count(char) # 利用內建方法 count 計算字元數量

# 測試函數
print(str_reverse("Hello World!"))  # 應該回傳 "!dlroW olleH"
print(count_char("Hello World!","l")) # 應該回傳 3