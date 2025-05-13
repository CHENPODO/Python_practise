"""
演示 JSON 數據和 Python 字典的相互轉換
"""
# 引入內建
import json
# 準備列表，列表內每一個元素都是字典，將其轉換成JSON
data = [{"name":"小陳","age":23},{"name":"Lee","age":23}]
"""
若輸入中文，卻未加入這段,ensure_ascii=False的話
在容器後會發生下方狀況
[{"name": "\u5c0f\u9673", "age": 23}, {"name": "Lee", "age": 23}]
"""
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)
# 準備字典，將字典轉換為JSON 數據類型[{k:v,k:v},{k:v,k:v}]
d = {"name":"小陳","age":23}
json_str = json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)
"""
<class 'str'>
{"name": "小陳", "age": 23}
"""
# 將 JSON 字符串轉換為 Python 數據類型{k:v,k:v}
s = '[{"name": "小陳", "age": 23}, {"name": "Lee", "age": 23}]'
d = json.loads(s)
print(type(d))
print(d)
"""
<class 'list'>
[{'name': '小陳', 'age': 23}, {'name': 'Lee', 'age': 23}]
"""