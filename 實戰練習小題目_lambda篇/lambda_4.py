"""
（進階邏輯題：filter + map + lambda）

完成以下任務：

- 用 filter() 搭配 lambda，篩選出大於 10 的數字。
- 接著用 map() 搭配 lambda，把篩選後的數字都加上 100。
- 把最後的結果轉成 list 並印出
"""
numbers = [3, 6, 9, 12, 15, 18, 21]

# 用 filter() 篩選出大於 10 的數字
bigThen10 = list(filter(lambda n:n > 10,numbers))
print(f"篩選大於 10 的數字結果是:{bigThen10}")

# 用 map() 把篩選後的數字加上 100
add100 = list(map(lambda add: add + 100 , bigThen10))
print(f"篩選後 + 100 的結果是:{add100}")
