"""
模塊導入
"""

# 使用 import 導入 time 模塊使用 sleep 功能(函數)
import time
print("哩賀恩賀?")
time.sleep(2) # 2 秒後執行下一句
print("賀!")

# 使用 from 導入 time 的 sleep功能(函數)
from time import sleep # 僅導入了 sleep()

print("哩賀恩賀?")
sleep(2) # 2 秒後執行下一句
print("賀!")

# 使用 * 導入 time 模塊的全部功能

from time import * # * -> 全引入
print("哩賀恩賀?")
sleep(2) # 2 秒後執行下一句
print("賀!")


# 使用 as 給特定功能加上別名
import time as T # 將 time 簡化成 T
print("哩賀恩賀?")
T.sleep(2)
print("賀!")
