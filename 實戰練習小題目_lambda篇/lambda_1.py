"""
題目 1（實作題）
請使用 lambda 寫一個可以傳入兩個參數 a 和 b，然後回傳 a 的 b 次方的匿名函數，並用 test_func() 執行它。
"""

def test_func(ab):
    result = ab(5,2) # 使用ab(參數)
    print(result)

test_func(lambda a,b : a ** b)