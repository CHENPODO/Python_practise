class Student:
    def __init__(self,name,age):
        self.name = name   # 學生姓名
        self.age = age     # 學生年齡

    # __str__ 魔術方法
    def __str__(self):
        return f"Student類對象，name:{self.name},age:{self.age}"
    # __lt__ 魔術方法
    def __lt__(self, other):
        return  self.age < other.age

    # __le__ 魔術方法
    def __le__(self, other):
        return  self.age <= other.age
    # __eq__ 魔術方法
    def __eq__(self, other):
        return self.age == other.age

stu = Student('abby',22)
stu1 = Student('apple',25)
# <__main__.Student object at 0x000002349E246900>
print(stu) # 列印結果唯一串地址值，須轉字串
print(stu > stu1) # False
print(stu <= stu1) # True
# 沒有寫__eq__ 的邏輯時，判斷則是默認內存地址
print(stu == stu1) # False

