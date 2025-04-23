"""
練習題1：找出成績最高的學生
請你寫一段程式：

- 使用 .keys() 取得所有的 key（學生名字）。

- 找出「分數最高的學生」是誰。

- 印出該學生的名字與分數。                                                                           ✅ 範例輸出格式：
"""

# 輸出結果是: 最高分是 Alice，分數是 95分

my_dict_stu = {
"Tom": 85,
"Alice": 95,
"Bob": 78,
"John": 60,
"Lucy": 88,
"Ken": 92,
"Emma": 74
}

All_keys = my_dict_stu.keys()
# print(All_keys)
# ['Tom', 'Alice', 'Bob', 'John', 'Lucy', 'Ken', 'Emma']
top_score = 0 # 先設定為0
top_score_name = "" # 先設定為空字串
for keys in All_keys:
    if my_dict_stu[keys] > top_score:
        top_score_name = keys
        top_score = my_dict_stu[keys]
print(f"最高分是{top_score_name},分數是{top_score}")