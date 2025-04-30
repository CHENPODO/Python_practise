"""
通過 windows的文本編輯器，將如下內容複製保存到: word.txt，文件可以存儲任意位置
最後通過文件讀取操作，讀取文件中???單詞出現次數

C:/Users/cindy/OneDrive/文件/word.txt"

Python is great. Learning Python can be fun. Python is powerful.

任務
- 將檔案 word.txt 存至任意可存取路徑
- 使用 Python 程式碼實作下列功能：
- 從該檔案中讀取文字。
- 統計指定單詞（例如 "Python"）出現的次數（區分大小寫或不區分大小寫都可以，但需說明）
將結果輸出至終端機。
"""
f = open("C:/Users/cindy/OneDrive/文件/word.txt","r",encoding="UTF-8")
print(type(f)) #<class '_io.TextIOWrapper'>

# readlines()
# lines = f.readline() # 指讀取一行
# lines = f.readlines()
# print(lines)

count = 0
# for
for line in f:
    print(line.strip())  # 顯示每行內容（去除換行符）
    count += line.count("Python")

f.close()
print(count)
