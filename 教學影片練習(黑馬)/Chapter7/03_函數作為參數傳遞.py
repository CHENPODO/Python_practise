"""
函數作為傳遞
"""

# 定義一個函數，接收另一個函數作為傳入參數
def test_func(compute):
    result = compute(1,2)
    print(f"compute 的類型是{compute}")
    print(result)
# 定義一個函數，準備作為參數傳入另一個函數
def compute(x,y):
    return x + y

# 調用，並傳入函數
test_func(compute)