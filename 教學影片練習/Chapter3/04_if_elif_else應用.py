# """
# if elif else
#
# """
#
# # 練習案例1
# print("歡迎來到XX動物園。")
# height = int(input("請輸入你的身高:"))
# vip_level =int(input("請你輸入你的vip級別(1~5): "))
# if height <= 120: # 若此處不成立
#     print("您的身高未超出120cm，可以免費遊玩!!") #不會列印
# elif vip_level > 3: # 若此處成立
#     print("您的VIP 級別大於 3 ，可免費遊玩~") # 會列印此行
# else:
#     print("您的身高超出120cm，請到售票處買票!") # 不會列印
#
# print("祝您遊玩愉快~") # 不再縮排中所以，會列印此行

# 練習案例:猜猜心裏數字

answer = 10

guess = int(input("請輸入第一次猜想的數字: "))
if guess == answer:
    print("猜對啦")
elif int(input("不對，再猜一次: ")) == answer :
    print("猜對啦")
elif int(input("不對，再猜最後一次: ")) == answer :
    print("猜對啦")
else:
    print("Sorry，全錯啦!我是猜10!")