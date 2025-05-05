"""
文件追加寫入
"""
# a 模式
#   - 文件不存在會創建文件
#   - 文件存在時，會追加在最後，寫入文件

f = open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/test_write.txt","a")
f.write("\nHello World is back!!") # 換行易看
f.close() # 內含 flush() 所以不用特別寫