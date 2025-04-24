def list_while_func():
    """
    使用 while 迴圈遍歷出列表演是函數
    :return: None
    """
    while_list = ["你好","我要練習","while遍歷"]
    # 迴圈控制變量通過下標索引來控制，默認0
    # 每一次迴圈將下標索引 +1
    # 循環條件: 下標索引變量 < 列表元素數量

    #定義一個變量來標記的下標
    index = 0 # 初始值為0
    while index < len(while_list):
        # 通過 index 變量取出對應下標的元素
        element = while_list[index]
        print(f"列表元素:{element}")

        # 將還變量(index)每一次循環 +1
        index += 1

list_while_func() # 調用執行


def list_for_func():
    """
    使用 for 迴圈遍歷出列表演是函數
    :return: None
    """
    for_list = [1,2,3,4,5]

    for element in for_list:
        print(f"列表元素有{element}")

list_for_func()

# 沒提示練習將while迴圈給遍歷出來
def while_list_func():
    while_list = [1,2,3,4,5]
    index = 0
    while index < len(while_list):
        element = while_list[index]
        print(element)
        index += 1
while_list_func()

# 沒提示練習將for迴圈給遍歷出來
def for_list_func():
    my_for_list = [1,2,3,4,5]
    for element in my_for_list:
        print(element)