"""
自定義模塊
"""

# 導入自定義模塊使用
from module_1 import add
add(1,3) # 4

# 導入不同模塊的同名功能
from module_1 import add
from module_2 import add
add(1,3) # -2，只會調用到module_2 中的 add

# __main__變量
from module_1 import add # 直接為4，因為在 module_1 已經跑add()了，決辦法是使用 __main__變量
add(1,3) # 4

# __all__變量
from module_1 import * # 星號全部導入，但因為在module_1 裡面設定了 __all__ 且無導入 sub() 所以會飄錯誤
# from module_1 import sub  # 手動引入可以
add(1,3) # 4
sub(1,3)