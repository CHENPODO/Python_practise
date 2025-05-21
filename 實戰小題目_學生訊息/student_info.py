"""
請設計一個類，計入學生的
姓名、年齡、地址

請實現:
- for循環，配合input輸入語句，並使用構造方法，完成學生訊息鍵盤錄入
- 輸入後使用print語句，完成輸出
"""

class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def display_info(self):
        print(f"name: {self.name}, age: {self.age}, address: {self.address}")

student_list = [] # 初始化學生列表為空，用來儲存學生物件
stu_count = int(input("輸入學生資料筆數: ")) # 輸入要建立的學生資料數量，用來控制迴圈次數
for stu in range(stu_count): # 使用 range(stu_count) 控制迴圈次數，依序輸入每筆學生資料
    input_name = input("請輸入姓名: ")
    input_age = input("請輸入年紀: ")
    input_address = input("請輸入地址: ")
    student = Student(input_name,input_age,input_address)
    student_list.append(student) # 根據輸入資料建立 Student 物件，並加入 student_list 中

for s in student_list:
    s.display_info() # 透過迴圈，直接跑方法