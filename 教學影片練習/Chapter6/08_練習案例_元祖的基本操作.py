"""
練習案例:元組的基本操作
"""

"""
請通過元組的功能(方法)，對其進行
1. 查詢其年齡所在的下標位置
2. 查詢學生的姓名
3. 刪除學生愛好中的football
4. 增加愛好:coding到愛好list內
"""
Student = ('周杰倫',11,['football','music'])
print(f"Q1、年齡的下標位置在: {Student.index(11)}")
print(f"Q2、學生名字為: {Student[0]}")
Student[2].remove('football')
print(f"Q3、刪除掉愛好中的愛好football,結果是: {Student}")
Student[2].append('coding')
print(f'Q4、增加愛好後的結果是: {Student}')
"""
要注意!!!
append() and remove() 並不會有返回值所以不可以直接透過列印輸出

print(f"Q4、增加愛好後的結果是: {Student[2].append('coding')}")
print(f"Q3、刪除掉愛好中的愛好football,結果是: {Student[2].remove('football')}")

"""
"""

Q1、年齡的下標位置在: 1
Q2、學生名字為: 周杰倫
Q3、刪除掉愛好中的愛好football,結果是: ('周杰倫', 11, ['music'])
Q4、增加愛好後的結果是: ('周杰倫', 11, ['music', 'coding'])

"""