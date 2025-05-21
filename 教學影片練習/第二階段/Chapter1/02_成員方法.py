class Student:
    name = None
    age = None

    def say_hi(self): # self 寫在類裡面時，會自動傳入self，除非要調用類裡面的屬性，否則外部變量是可以不用使用他的
        print(f"你好，我是 {self.name}")

    def say_hi2(self,msg):
        print(f"你好啊，我是{self.name}，{msg}")
# 透過stu這個容器把類接收
stu = Student()
stu_2 = Student()
stu.name = 'Amy' # 附值
stu.say_hi() # 調用了 say_hi()

stu_2.name = 'Tae'
stu_2.say_hi2("請多指教")