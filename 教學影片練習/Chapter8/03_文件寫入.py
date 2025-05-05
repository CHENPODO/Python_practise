"""
文件寫入
"""
# import time
# 打開文件，不存在的文件
f = open("C:/Users/cindy/OneDrive/桌面/Python_practise/教學影片練習/Chapter8/test_write.txt","w",encoding="UTF-8")

# write 寫入
f.write("ha ha changed!") # 內容寫入內存
"""
原本為"hello world!"
但是因為是 "w" 模式，所以若是原本就有的檔案在一開始就會被清空
"""
# time.sleep(600000)

# flush()刷新
f.flush() # 將內存中的內容，寫入到硬碟的文件中
# close() 關閉
f.close()
# 打開一個存在的文件

# write寫入、flush 刷新

# close() 關閉