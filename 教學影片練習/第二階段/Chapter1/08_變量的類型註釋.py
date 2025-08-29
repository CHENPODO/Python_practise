# 變量 設置類型註解
# 基礎語法: 變量:類型
import json
import random

var_1:int = 10
var_2:float = 3.14
var_3: bool = True
var_4:str = "IT_CAST"

# 類對象類型註釋
class Students:
    pass

stu:Students = Students()

# 基礎容器類型註解
my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_set:set = {1,2,3}
my_dict:dict = {"a":1,"b":5}
my_str:str = "IT"

# 基礎容器類型詳細註解
my_list_2:list[int] = [1,2,3]
my_tuple_2:tuple[str,int,bool] = ("IT",555,True)
my_set_2:set[int] = {1,2,3}
my_dict_2:dict[str,int] = {"a":1,"b":5}
# - 元組類型設置類型詳細註解，需要算標記出來
# - 字典類型設置類型詳細註解，需要兩個類型，第一個是key，第二個是value

# type:類型
# 在註釋中進行類型註釋
import json
import random

# 在註釋中進行類型註釋 (舊式寫法)

# json.loads() 函式需要一個 JSON 字串作為輸入
data = '{"a": 1, "b": 2}'
var2_ver2 = json.loads(data)          # type: dict[str, int]

var1_ver2 = random.randint(1, 10)     # type: int

# 定義一個名為 Student 的類別
class Student:
    pass

# func 是一個 Student 類別的實例，其類型為 Student
func = Student()             # type: Student
