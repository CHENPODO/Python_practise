"""
案例練習
需求: 有一份帳單文件，紀錄消費收入的
"""
f= open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/bill.txt","w")
data = [
    "Alice,2025-05-01,120,正式\n",
    "Bob,2025-05-02,80,測試\n",
    "Charlie,2025-05-02,250,正式\n",
    "David,2025-05-03,300,測試\n",
    "Eve,2025-05-03,500,正式\n",
    "Frank,2025-05-04,90,測試\n",
    "Grace,2025-05-04,180,正式"]

for nameList in data:
    f.write(nameList)
    print(nameList.strip())

# f.write()
f.close()