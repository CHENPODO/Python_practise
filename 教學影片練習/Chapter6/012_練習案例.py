"""
練習案例: 序列的切片實踐

有字符串:"萬過薪月,員序程馬黑,nohtyP學"
- 請使用學過的任何方式,得到 "黑馬程序員"
"""

"""
# 解法(自己想)
string = "萬過薪月,員序程馬黑來,nohtyP學"
str_1 = string.split(",")
# print(str_1) ['萬過薪月', '員序程馬黑來', 'nohtyP學']
str_result1 = str_1[1]
# print(str_result1)
result_end = str_result1[4::-1]
print(result_end)
"""

# 解法1 倒序字符串，然後切片取出
"""
strA = "萬過薪月,員序程馬黑來,nohtyP學"
res_1 = strA[::-1][9:14:1]
print(res_1)
"""

# 解法2 切片取出然後倒序
"""
strA = "萬過薪月,員序程馬黑來,nohtyP學"
result_2 = strA[5:10:1][::-1]
print(result_2)
"""

# 解法3
# 可參考split 分隔 "," ，replace 替換 "來" 為空,到序字符串
strA = "萬過薪月,員序程馬黑來,nohtyP學"
result_3 = strA.split(",")[1].replace("來","")[::-1]
print(result_3)