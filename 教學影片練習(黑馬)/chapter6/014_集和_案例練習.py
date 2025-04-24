"""

信息去重

my_list = ['黑馬程序員','傳智播客','黑馬程序員','傳智播客','iteima','itcast','iteima','itcast','best']

- 定義一個空集合
- 通過for遍立列表
- for循環中將列表的元素添加到集合
- 最終得到元素去重後的集合對象，並打印輸出

"""
my_set = set() # 新增一個空集合
my_list = ['黑馬程序員','傳智播客','黑馬程序員','傳智播客','iteima','itcast','iteima','itcast','best']
for item in my_list:
    my_set.add(item)
print(my_set)

