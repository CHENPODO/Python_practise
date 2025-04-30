"""
演示數據容器的適用功能
"""

my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,}

# len 元素數量

print(f"列表元素數量有:{len(my_list)}")
print(f"元組元素數量有:{len(my_tuple)}")
print(f"字符串元素數量有:{len(my_str)}")
print(f"集合元素數量有:{len(my_set)}")
print(f"字典元素數量有:{len(my_dict)}")

# 輸出結果如下
"""

列表元素數量有:5
元組元素數量有:5
字符串元素數量有:7
集合元素數量有:5
字典元素數量有:4

"""

# max 最大元素
print(f"列表最大元素有:{max(my_list)}")
print(f"元組最大元素有:{max(my_tuple)}")
print(f"字符串最大元素有:{max(my_str)}")
print(f"集合最大元素有:{max(my_set)}")
print(f"字典最大元素有:{max(my_dict)}")


# 輸出結果如下
"""

列表最大元素有:5
元組最大元素有:5
字符串最大元素有:g
集合最大元素有:5
字典最大元素有:key4

"""

# min 最小元素

# max 最大元素

print(f"列表最小元素有:{min(my_list)}")
print(f"元組最小元素有:{min(my_tuple)}")
print(f"字符串最小元素有:{min(my_str)}")
print(f"集合最小元素有:{min(my_set)}")
print(f"字典最小元素有:{min(my_dict)}")


# 輸出結果如下
"""

列表最小元素有:1
元組最小元素有:1
字符串最小元素有:a
集合最小元素有:1
字典最小元素有:key1

"""

# 類型轉換:容器轉列表

print(f"元組轉列表:{list(my_tuple)}")
print(f"字符串轉列表:{list(my_str)}")
print(f"集合轉列表:{list(my_set)}")
print(f"字典轉列表:{list(my_dict)}")


# 輸出結果如下

"""

元組轉列表:[1, 2, 3, 4, 5]
字符串轉列表:['a', 'b', 'c', 'd', 'e', 'f', 'g']
集合轉列表:[1, 2, 3, 4, 5]
字典轉列表:['key1', 'key2', 'key3', 'key4']

"""

# 轉元組

print(f"列表轉元組:{tuple(my_list)}")
print(f"字符串轉元組:{tuple(my_str)}")
print(f"集合轉元組:{tuple(my_set)}")
print(f"字典轉元組:{tuple(my_dict)}")


# 輸出結果如下
"""

列表轉元組:(1, 2, 3, 4, 5)
字符串轉元組:('a', 'b', 'c', 'd', 'e', 'f', 'g')
集合轉元組:(1, 2, 3, 4, 5)
字典轉元組:('key1', 'key2', 'key3', 'key4')

"""

# 轉字符串

print(f"列表轉字符串:{str(my_list)}")
print(f"元組轉字符串:{str(my_tuple)}")
print(f"集合轉字符串:{str(my_set)}")
print(f"字典轉字符串:{str(my_dict)}")


# 輸出結果如下
"""

列表轉字符串:[1, 2, 3, 4, 5]
元組轉字符串:(1, 2, 3, 4, 5)
集合轉字符串:{1, 2, 3, 4, 5}
字典轉字符串:{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

"""


# 轉集合

print(f"列表轉集合:{set(my_list)}")
print(f"元組轉集合:{set(my_tuple)}")
print(f"字符串轉集合:{set(my_str)}")
print(f"字典轉集合:{set(my_dict)}")


# 輸出結果如下
"""

列表轉集合:{1, 2, 3, 4, 5}
元組轉集合:{1, 2, 3, 4, 5}
字符串轉集合:{'f', 'c', 'a', 'b', 'd', 'g', 'e'} # 因為set()，是無序化
字典轉集合:{'key2', 'key4', 'key1', 'key3'} 無序化

"""

# sorted 排序 的結果會通通變成列表對象
my_list = [3,1,2,5,4]
my_tuple = (3,1,2,5,4)
my_str = "bdcefga"
my_set = {3,1,2,5,4}
my_dict = {"key3":3,"key1":1,"key2":2,"key5":5,"key4":4,}

print(f"列表對象的排序結果{sorted(my_list)}")
print(f"元組對象的排序結果{sorted(my_tuple)}")
print(f"字符串對象的排序結果{sorted(my_str)}")
print(f"集合對象的排序結果{sorted(my_set)}")
print(f"字典對象的排序結果{sorted(my_dict)}")

# 輸出結果如下

"""

列表對象的排序結果[1, 2, 3, 4, 5]
元組對象的排序結果[1, 2, 3, 4, 5]
字符串對象的排序結果['a', 'b', 'c', 'd', 'e', 'f', 'g']
集合對象的排序結果[1, 2, 3, 4, 5]
字典對象的排序結果['key1', 'key2', 'key3', 'key4', 'key5']

"""

# sorted 反向排序 加上 ,reverse = True
my_list = [3,1,2,5,4]
my_tuple = (3,1,2,5,4)
my_str = "bdcefga"
my_set = {3,1,2,5,4}
my_dict = {"key3":3,"key1":1,"key2":2,"key5":5,"key4":4,}

print(f"列表對象的反向排序結果{sorted(my_list, reverse=True)}")
print(f"元組對象的反向排序結果{sorted(my_tuple, reverse=True)}")
print(f"字符串對象的反向排序結果{sorted(my_str, reverse=True)}")
print(f"集合對象的反向排序結果{sorted(my_set, reverse=True)}")
print(f"字典對象的反向排序結果{sorted(my_dict, reverse=True)}")

# 輸出結果如下

"""

列表對象的反向排序結果[5, 4, 3, 2, 1]
元組對象的反向排序結果[5, 4, 3, 2, 1]
字符串對象的反向排序結果['g', 'f', 'e', 'd', 'c', 'b', 'a']
集合對象的反向排序結果[5, 4, 3, 2, 1]
字典對象的反向排序結果['key5', 'key4', 'key3', 'key2', 'key1']

"""