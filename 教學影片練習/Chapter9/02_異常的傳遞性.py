"""
函數之中有傳遞姓
"""

# 定義一個出現異常的方法
def func1():
    print("func1開始運行!")
    1 / 0 # 這會報錯，除0錯誤
    print("func1結束運行!")
# 定義一個無異常的方法
def func2():
    print("func2開始運行!")
    func1()
    print("func3結束運行!")
# 定義一個方法，調用上面的方法
def main():
    try:
        func2()
    except Exception as e:
        print(f"抓到錯誤了，錯誤名稱是: {e}")

main() # 調用
"""
func2開始運行!
func1開始運行!
抓到錯誤了，錯誤名稱是: division by zero

"""