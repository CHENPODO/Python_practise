"""
try:
   可能發生錯誤的區塊
expect:
    若是異常則執行此區塊
"""
# 基本語法
"""
try:
    # 因為無該檔案
    f = open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/CatchBug.txt","r",encoding="UTF-8")
except:
    print("抓到bug啦!")
# 捕獲指定異常
try:
    print(name)
except NameError as e:
    print(e) # 打印錯誤 name 'name' is not defined
    print("name 未定義")
# 捕獲多個異常
try:
    print(1/0)
except (NameError,ZeroDivisionError) as e:
    print(e)  # 打印錯誤 division by zero
    print("出現了變量未定義 或者 除以 除以8的異常錯誤")
"""
# 未正確設置捕獲異常類型，將無法捕獲異常

# 捕獲所有異常
"""
try:
    1 / 0
except Exception as e:
    print("出現異常了!")
    """

# 異常else
"""
try:
    print(1)
except Exception as e:
    print("出現異常了!")
else:
    print("呀哈!沒有bug，成功運行啦!!")
    """
# finally
try:
    f = open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/test_write.txt", "r",encoding="UTF-8")
except Exception as e:
    print(e)
    f = open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/test_write.txt", "r",encoding="UTF-8")
else:
    print("呀哈!沒有bug，成功運行啦!!")
finally:
    f.close() # 一定會執行
    print("我是finally，有沒有異常我都要執行!!")