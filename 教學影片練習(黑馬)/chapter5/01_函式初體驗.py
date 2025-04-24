"""
演示:快速體驗函數的開發及應用
"""
# 需求: 統計字符串長度，不使用內自函數 len()

str1 = "itheima"
str2 = "itcast"
str3 = "python"
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}，長度是: {count}")
my_len(str1)
my_len(str2)
my_len(str3)


"""
# 執行一個hi()
def hi():
    print("hello")
hi() # hello
"""