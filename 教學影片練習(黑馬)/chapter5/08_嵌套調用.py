"""
函數的嵌套調用
"""

def func_b():
    print("---2---")

def func_a():
    print("---1---")

    func_b()

    print("---3---")

# 調用
func_a()