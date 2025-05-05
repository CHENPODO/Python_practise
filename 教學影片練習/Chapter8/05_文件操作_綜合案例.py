"""
案例練習
需求: 有一份帳單文件，紀錄消費收入的，列印出來

- 練習2
    - open 和 r 模式打開一個文件對象，並且讀取文件
    - open 和 r 模式打開另一個文件對象，用於文件寫出
    - 跑內容，判斷是否是測試不是測試就write寫出，是測試就continue跳過
    - 將2個對象均 close()
"""

f= open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/bill.txt","r",encoding="UTF-8")

# test2
f_out = open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/bill_formal.txt", "w",encoding="UTF-8")
for New in f:
    if "測試" in New:
        continue
    f_out.write(New)
    print(New.strip())

# f.write()
f.close()
f_out.close()