"""
1. 數字隨機產生
2. 有3次機會猜測，通過3層嵌套
3. 每次猜不種會提是猜大或是猜小了
"""
# 提示，通過如下程式碼，定義變量 num ，變量內存隨機數字
# 1. 構建一個隨機數
import random
num = random.randint(1,10)
# print(num)

# 2.
guess_num = int(input("你要猜測的數字: "))
if guess_num == num:
    print("恭喜猜對啦!")
else:
    if guess_num > num:
        print("猜大了")
    else:
        print("猜小了")
    guess_num = int(input("你第二次要猜測的數字: "))
    if guess_num == num:
        print("恭喜猜對啦!")
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")
            guess_num = int(input("你第三次要猜測的數字: "))
            if guess_num == num:
                print("恭喜猜對啦!")
            else:
                if guess_num > num:
                    print("猜大了")
                else:
                    print("三次機會都猜錯了!!")
