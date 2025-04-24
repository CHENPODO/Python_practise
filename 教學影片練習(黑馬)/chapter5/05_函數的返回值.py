"""
演示: 定義函數返回值的語法格式
"""
# 定義一個函數，完成2數相加功能
def add(a,b):
    res = a + b
    return  res
# 通過返回值，將相加結果返回給調用者
r = add(2,3)
print(r)