"""
題目 2（應用題）
有一個清單 numbers = [1, 2, 3, 4, 5]
請用 map() 搭配 lambda 函數，把清單中每個數字都平方，並把結果轉成 list 印出。
"""

numbers = [1, 2, 3, 4, 5]

# 須轉為列表沒轉的話會列印出非列表的結果
# map()是一個可迭代的物件（iterator / map object）
result = list(map(lambda n: n * n,numbers))
print(result)