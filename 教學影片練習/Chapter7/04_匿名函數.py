"""
lambda 匿名函數 
"""

def test_func(compute):
    result = compute(1,3)
    print(result)

#         關鍵字  參數 : 函數體
test_func(lambda x,y : x + y)