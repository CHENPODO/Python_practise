"""
方法
"""

"""
class Student:
    def add(self,x,y):
        return x+y
print(Student().add(1,2))
"""

# 透過index列印該元素的下標
"""
list1 = ['a','b','c']
print(list1.index('b')) # 1
"""

# 修改元素值
"""
list1 = ['a','b','c']
list1[0] = 'd'
print(list1) #['d','b','c']
"""
# 插入元素 insert
"""
list1 = ['a','b','c']
list1.insert(1,'yan')
print(list1) # ['a', 'yan', 'b', 'c']
"""

# 追加 append
"""
list1 = ['a','b','c']
list1.append('d') # 在尾部加入'd'
print(list1) # ['a', 'b', 'c', 'd']
"""
# 追加元素 2 .extend
"""
listA= [1,2,3]
listA.extend([4,5,6])
print(listA) # [1,2,3,4,5,6]
"""
# del 列表[下標]
"""
listA= [1,2,3]
del listA[0]
print(listA) # [2,3]
"""
# 列表.pop[下標]
"""
listA= [1,2,3]
element = listA.pop(0)
print(f"通過此方法取出後的陣列為{listA},而我所取出的元素為: {element}")
"""

# 刪除某元素在列表中的第一個匹配項
"""
listA= [1,2,3,2,3]
listA.remove(2)
print(listA) # [1,3,2,3]
"""
# 清空列表
"""
listA= [1,2,3]
listA.clear()
print(listA) # []
"""
# 統計列表內某元素的數量 .count
"""
listA= [1,2,3,2,3]
print(listA.count(3)) # 2
"""
# 統計列表中的全部數量
listA= [1,2,3,2,3]
print(len(listA)) # 5