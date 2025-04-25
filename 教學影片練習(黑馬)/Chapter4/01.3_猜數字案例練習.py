"""
無限次機會
每一次猜不中，會提示猜大或猜小
猜完數字後會提示猜了幾次
"""

# 獲取0~10隨機數
import random
num = random.randint(0,10)
# print(num)

# 通過flag變量設置成布爾類型，循環是否繼續
flag = True
# 新增一個計算的變量
count = 0

while flag :
    # 猜測數字帶入 input 語句
    guess_num = int(input("請輸入猜測的數字: "))
    count += 1 #每一輪都 += 1，計算猜測次數
    if guess_num == num:
        print("猜對了!")
        flag = False
    else:
        if guess_num > num:
            print("笑鼠你猜大啦!")
        else:
            print("你猜小啦!再多點!")
print(f"你總共猜了{count}次!")
