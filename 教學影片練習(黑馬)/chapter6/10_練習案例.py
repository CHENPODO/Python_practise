"""
練習案例: 分割字符串

給定一個字符串: "itheima itcast boxuegu"
- 統計字符串內有多少個"it"字符
- 將字符串內的空格，全部替換為字符:"|"
- 並按照"|"進行字符串分割，得到列表
"""
# 提示: count、replace、split
String = "itheima itcast boxuegu"
count = String.count("it")
change_String = String.replace(" ","|")
print(f"原來是: {String}，更改後 {change_String}")
# split
new_list = change_String.split("|")
print(f"原來是: {change_String}，更改後 {new_list}")
