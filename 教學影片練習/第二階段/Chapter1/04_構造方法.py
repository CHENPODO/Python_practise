# 使用構造方法對成員變量進行附值

# 構造方法的名稱 __init__ -> 自動執行

class Student:
    name = None # 可省略
    age = None # 可省略
    tel = None # 可省略

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("成功建立成員變量附值")

stu = Student('Amy',18,'012345789')
print(stu.name,stu.age,stu.tel)