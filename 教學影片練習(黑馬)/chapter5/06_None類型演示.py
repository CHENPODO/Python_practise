"""
演示: None
"""
"""# 不 return 語句的函數返回值
def hi():
    print("Hi!")
res = hi()
print(res)
print(type(res))
"""
"""
# 這兩行意思幾乎等價：
res = hi()   # 呼叫 hi() 的同時，把返回結果給 res
hi()         # 單純呼叫，執行內容，但不接住回傳值
"""

# 主動返回 return函數
"""def hi():
    print("Hi!")
    return None  # 強調這是一個只有副作用的函式 
res = hi()
print(res)
print(type(res))
"""
"""
# None 用於 if 判斷
def age(age):
    if age > 18:
        return "Success"
    else:
        return None

res = age(16)
if not res:
    print("未成年不可以進入該空間")
"""
# None用於聲明無初始值的變量

name = None
print(name)