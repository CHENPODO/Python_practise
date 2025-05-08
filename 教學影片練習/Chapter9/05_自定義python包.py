"""
python 包
"""

# 創建一個包
# 導入自訂一的包中的模塊，並使用
from module_package import module_1
from module_package import module_2

module_1.func1_print() # func1_print
module_2.func2_print() # fun2_print

# 通過__all__變量，控制import
# 要在__init__.py

from  module_package import *
module_1.func1_print() # func1_print
module_2.func2_print() # fun2_print