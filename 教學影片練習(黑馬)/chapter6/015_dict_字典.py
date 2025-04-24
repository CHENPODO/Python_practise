"""
演示 字典 dict
"""

# 定義字典
# {"小伊":98,"小岩":87,"小泰":78}

# 定義空字典
# 方法1
my_dict = {}
# 方法2
my_dict2 = dict()

# 定義重複 key 的字典
# my_dict3 = {"小伊":98,"小岩":87,"小泰":78 "小伊":98}

# 從字典中基於 key 獲取 Value
my_dict3 = {"小岩":87,"小泰":78,"小伊":98}
score = my_dict3["小岩"]
print(f"小岩的考試分數是:{score}")
score = my_dict3["小泰"]
print(f"小泰的考試分數是:{score}")

# 定義嵌套字典
my_dict3 = {
    "小岩": {
            "數學":60,
            "自然":71
            },
    "小泰":{
            "數學":86,
            "自然":75
            },
    "小伊":{
            "數學":50,
            "自然":88
            },
}


# 從嵌套字典中獲取數據
print(my_dict3["小伊"]["數學"])



# 新增元素
my_dict_stu = {"小岩":87,"小泰":78,"小伊":98}
my_dict_stu["源源"]=88
print(f"新增源源成績的結果是:{my_dict_stu}")

# 更新元素
my_dict_stu["小泰"]=78
print(f"更新小泰成績的結果是:{my_dict_stu}")


# 刪除元素
yan_score = my_dict_stu.pop("小岩")
print(f"刪除小岩成績的結果是:{my_dict_stu},小岩的成績是{yan_score}")


# 清空元素
"""
my_dict_stu.clear()
print(f"清空元素的結果是:{my_dict_stu}")
"""


# 獲取全部的key
AllKeys = my_dict_stu.keys()
print(f"獲取全部的key的結果是:{AllKeys}")

# 遍歷字典
# 方式1
for key in my_dict_stu:
    print(key,my_dict_stu[key])
# 方式2
for key in AllKeys:
    print(key,my_dict_stu[key])

# 統計字典裡的元素數量
num = len(my_dict_stu)
print(num)