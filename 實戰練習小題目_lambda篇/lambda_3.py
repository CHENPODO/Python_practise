"""
題目 3（進階應用題：filter）
有一個清單 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，
請用 filter() 搭配 lambda 函數，篩選出偶數，並把結果轉成 list 印出。

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda n: n % 2 == 0,numbers))
print(even_list)