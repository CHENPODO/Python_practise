"""
模擬在控制台操作 XX銀行

- 定義全局變量:money，用來記錄銀行卡餘額(默認5000000)
- 定義全局變量:name,用來記錄客戶姓名(啟動程序時輸入)

定義如下函數
 - 查詢餘額函數
 - 存款函數
 - 取款函數
 - 主菜單函數

- 要求:
- 程序啟動後要求輸入客戶姓名
- 查詢餘額、存款"取款後都會返回主菜單
- 存款、取款後，都應顯示一下當前餘額
- 客戶選擇退出或輸入錯誤，程序都會退出，否則一直運行
"""
# 定義全局變量
money = 5000000
name = input("請輸入客戶姓名: ")

# 歡迎畫面
def start():
    print(f"\n{name}，您好，歡迎來到XX銀行\n")

# 查詢餘額
def find():
    print("--------------查詢餘額--------------")
    print(f"{name}，您的當前餘額為：{money} 元\n")

# 存款
def save():
    print("--------------存款--------------")
    global money
    amount = int(input("請輸入存款金額: "))
    money += amount
    print(f"{name}，您好，存款成功！目前餘額為：{money} 元\n")

# 取款
def takeMoney():
    print("--------------取款--------------")
    global money
    amount = int(input("請輸入取款金額: "))
    if amount > money:
        print("餘額不足，取款失敗!\n")
    else:
        money -= amount
        print(f"{name}，您好，成功取款 {amount} 元，目前餘額為 {money} 元。\n")

# 主選單
def homeMenu():
    while True:
        print("--------------主菜單--------------")
        print(f"{name}，您好，歡迎使用XX ATM，請選擇操作:")
        print("1. 查詢餘額")
        print("2. 存款")
        print("3. 取款")
        print("4. 退出")
        choice = input("請輸入選項（1~4）: ")

        if choice == '1':
            find()
        elif choice == '2':
            save()
        elif choice == '3':
            takeMoney()
        elif choice == '4':
            print("謝謝使用，歡迎再次光臨！")
            break
        else:
            print("輸入錯誤，即將退出！")
            break

# 啟動
start()
homeMenu()