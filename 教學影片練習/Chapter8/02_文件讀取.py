"""
- 想保存數據，可使用 硬碟、 USB 、DVD(燒入)等...來儲存數據

- 一般文件可分為
    1. 文本文件
    2. 影像文件
    3. 音頻文件
    4. 圖片文件
    ...等...類別

- 文件操作包含甚麼內容?
    1. 打開文件
    2. 讀寫文件
    3. 關閉文件

- 注意: 可以只打開和關閉文件，不進行任何讀寫

- open() 打開函數
    - python 中，使用 open() 函數，可以打開一個已經存在的文件，或是創建新文件
    語法 -> open(name,mode,encoding)
    name : 是要打開目標文件名的字符串(可包含具體路徑)
    mode : 設置打開文件的模式(訪問模式):只讀、寫入、追加等
    encoding : 編碼格式(推薦使用 UTF-8)
Ex.
f=open('python.txt','r',encoding = 'UTF-8')
# encoding的順序不是第三位，所以不能用位置參數，用關鍵字參數直接指定


- mode 常用基礎訪問模式
1. r(read) -> - 用來讀取已存在的文件
        - 如果檔案不存在，會產生錯誤（FileNotFoundError）
        - 檔案指標會停在檔案開頭
2. w(write) -> - 用來寫入資料
        - 若檔案已存在，會先清空原內容再寫入
        - 若檔案不存在，會自動新建一個檔案
3. a(append) -> - 用來**附加（加在原內容後）**資料
                - 若檔案不存在，會自動新建一個檔案
                - 若檔案存在，新的資料會接在原內容之後，不會清除原資料
"""

# 演示

# 打開文件
f = open("C:/Users/cindy/OneDrive/文件/測試.txt","r",encoding="UTF-8")
print(type(f)) #<class '_io.TextIOWrapper'>

# 讀取文件 - read()
print(f"讀取2個字節是:{f.read(2)}") # 讀取2個字節是:測試
# print(f"讀取2個字節是:{f.read()}")  # 讀取2個字節是:.txt

# 讀取文件 - readlines()

lines = f.readlines()  # 每一行是一個字串元素，含 \n
print("用 readlines() 讀取的內容：", lines)

# 讀取文件 - readline()
"""
readline() 一次只讀取一行，適合處理大型文件或逐行處理
每次呼叫都會從當前位置繼續讀下一行
回傳值是一個字串，包含換行符號 \n（除非是最後一行）

假設:測試.txt
第一行資料
第二行資料
第三行資料


"""
f = open("C:/Users/cindy/OneDrive/文件/測試.txt", "r", encoding="UTF-8")

print(f.readline())  # 第一行資料\n
print(f.readline())  # 第二行資料\n
print(f.readline())  # 第三行資料



# for
for i in f:
    print(i)

# 關閉
f.close()
# with open()
"""
通過在 with open() 的語句中隊文件進行操作
可在操作完成後自動關閉 close()
"""