"""
演示 set()
數據內容集合使用
"""

# 定義集合
num = {1, 2, 3, 4, 5, 1} # 可以注意到數字1並無重複
setExample = set()
print(f"num 的內容是{num}，類型是{type(num)}")
print(f"setExample 的內容是{setExample}，類型是{type(setExample)}")
"""
num 的內容是{1, 2, 3, 4, 5}，類型是<class 'set'>
setExample 的內容是set()，類型是<class 'set'>
"""
# 添加新元素
stringExample = { "a", "b", "c"}
stringExample.add("d")
stringExample.add("a") # 只會有1個
# 這是正確的行為說明：
# "a" 不會重複出現
# "d" 會被加進去
# 但集合的輸出順序可能不同

print(f"stringExample 添加後為: {stringExample}")

# 移除元素
stringExample = { "a", "b", "c"}
stringExample.remove("a")
print(f"使用移除方法{stringExample}") # 使用移除方法{'b', 'c'}

# 隨機取出一個元素 pop()
stringExample = { "a", "b", "c"}
element = stringExample.pop()
print(f"使用隨機取出方法{element}") # 使用移除方法{'b', 'c'}
print(f"再度列印可確認{stringExample}已經移除某元素")

# 清空集合 clear
stringExample = { "a", "b", "c"}
stringExample.clear()
print(f"使用清空集合後結果為: {stringExample}")

# 取2個集合的差集 .difference()
set_1 = {1, 2, 3}
set_2 = {1,5,6}
set_3 = set_1.difference(set_2) # 集合1有 而 集合2 沒有的東西抽出來
print(f"取出差集後結果: {set_3}") # {2,3}
print(f"取出差集後 set_1 :{set_1}") # 不變
print(f"取出差集後 set_2 :{set_2}") # 不變

# 消除2個集合的差集
set_1 = {1, 2, 3}
set_2 = {1, 5, 6}
# 集合1中，刪除和集合2相同的元素(集合1更改/集合2不更動)
set_3 = set_1.difference_update(set_2)
print(f"消除出差集後結果: {set_3}") # None
print(f"消除差集後 set_1 :{set_1}") # {2,3}
print(f"消除差集後 set_2 :{set_2}") # {1, 5, 6}

# 2個集合合併為1個
set_1 = {1, 2, 3}
set_2 = {1, 5, 6}
# unior()的方法會將傳入新集合
set_3 = set_1.union(set_2)
print(f"合併差集後結果: {set_3}") # {1,2,3,5,6}
print(f"合併差集後 set_1 :{set_1}") # {1, 2, 3} 不變
print(f"合併差集後 set_2 :{set_2}") # {1, 5, 6} 不變
"""
合併差集後結果: {1, 2, 3, 5, 6}
合併差集後 set_1 :{1, 2, 3}
合併差集後 set_2 :{1, 5, 6}

"""

# 統計集合元素數量 len()
total_set = len(set_3)
print(f"統計集合元素數量: {total_set}")
"""
統計集合元素數量: 5
"""

# 集合的遍歷
for i in set_3:
    print(i)

"""
1
2
3
5
6

"""