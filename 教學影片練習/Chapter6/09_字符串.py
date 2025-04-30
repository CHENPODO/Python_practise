"""
演示以數據容器的角色，學習字符串的相關操作
"""

# 定義一個容器
string = "This is a string"
# 通過下標索引取數值
# 先創造一個容器接收string個字符串
getString = string
print(getString[0]) # T
# index 方法
getString.index("a")
print(f"起始下標是{getString.index("a")}") #8
print(f"總共有多少index:{len(getString)}") #總共有多少index:16
# replace 方法
# 語法: 字符串.replace("字符串1","字符串2")
"""
，將 "字符串1"裡的內容換成 "字符串2"，但並不會把原有的字符串修改，而是需要新的接收容器
"""
new_box = getString.replace("This","這是")
print(f"原有修改後的字符串容器是 getString 結果是:{getString}，新的接收容器為 new_box 結果是 :{new_box}")

# split 方法
# 語法: 字符串.split() =>透過一個容器接收並將結果傳入，印出來的結果會是一個對象列表

result = getString.split(" ")

print(f"分割方法 split() 會列印出的結果是: {result}")

# strip() 方法
# 1. (去前後空格) 語法: 字符串.strip()
string = " itYan and itcast"
print(f"原本是: {string}， 去前後空格，結果是:{string.strip()}")
# 2. (去指定字符串) 語法:  字符串.strip("12") # 原本是:  itYan and itcast， 去前後空格，結果是:itYan and itcast
string = "12itYan and itcast12"
print(f"原本是: {string}， 去前後空格，結果是:{string.strip("12")}") # 原本是: 12itYan and itcast12， 去前後空格，結果是:itYan and itcast
# 統計字符串中某字符串的出現次數  count()
string = "it is itcast it is itcast"
new_count = string.count("it")
print(new_count) # 4
# 統計字符串長度
string = "it dog"
new_count = len(string)
print(new_count) # 6

# while 遍歷字符串
string = "小黑工程師"
i = 0
while i < len(string):
    print(string[i])
    i += 1

# for
string = "it"
for i in string:
    print(i)