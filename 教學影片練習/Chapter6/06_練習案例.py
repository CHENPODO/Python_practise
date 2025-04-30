"""
定義一個列表，內容是:[1,2,3,4,5,6,7,8,9,10]
- 遍歷列表，取出列表內的偶數，並存入一個新的列表對象中
- 使用 while 迴圈和 for 迴圈個操作一次
"""
from operator import index


# 提示
# - 通過 if 判斷來確認偶數
# - 通過列表的 append 的方法，來增加元素

def while_list_func():
    while_list = [1,2,3,4,5,6,7,8,9,10]
    index = 0
    new_list = [] # 新列表
    while index < len(while_list):
        element = while_list[index]
        if element % 2 == 0:
            new_list.append(element)
        index += 1
    print(f"通過 while迴圈，從列表:{while_list}中取出偶數，組成新列表: {new_list}")

while_list_func()

# for
def for_list_func():
    for_list = [1,2,3,4,5,6,7,8,9,10]
    new_list = []
    for element in for_list:
        if element % 2 == 0:
            new_list.append((element))
    print(f"通過 for迴圈，從列表:{for_list}中取出偶數，組成新列表: {new_list}")

for_list_func()