"""
判斷語句嵌套
"""
from sys import int_info

# 小練習
# print("歡迎來到XX動物園!!")
# if int(input("請輸入你的身高: ")) > 120:
#     print("需進行補票!!")
#     print("但如果是VIP3以上幾可免費入園!")
#     if int(input("告訴我你的Vip級別是: ")) > 3:
#         print("歡迎貴賓，您可以免費入園遊玩!")
#     else:
#         print("請至櫃台補票入場")
# else:
#     print("免費入園小朋友~~")

# 小練習2
age = int(input("你的年齡: "))
if 18 <= age < 30:
    print("可以領取但要檢查您的年資!")
    if int(input("你的年資是: ")) > 3 :
        print("確認成功!你可以領取")
    else:
        print("取得失敗")
else:
    print("取得失敗")
