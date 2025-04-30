"""
4種常見參數使用演示
"""

"""
- 位置參數
- 關鍵字參數
- 缺省參數(默認函數)
- 不定長函數
"""

# 位置參數

def user_info_1(name,age,gender):
    print(f"姓名是:{name},年紀是:{age},性別是{gender}")
user_info_1("andy",28,"boy")

# 關鍵字參數
"""
關鍵傳參可以不照順序
可混合位置傳參數使用，但位置參數必須在前
"""

def user_info_2(name,age,gender):
    print(f"姓名是:{name},年紀是:{age},性別是{gender}")
user_info_2(name="noa",age=22,gender='girl') # 關鍵字傳參數
user_info_2(name="noa",gender='girl',age=22) # 可不照順序
user_info_2("noa",age=22,gender='girl') # 關鍵字、位置傳參數混合


# 缺省參數
def user_info3(name,gender,age=18): # 默認值要放在最後
    print(f"姓名是:{name},年紀是:{age},性別是{gender}")
user_info3("min",'girl') # 默認值 -> 年齡
user_info3("minx",'girl',age = 20) # 更改默認值 -> 年齡

# 不定長函數
# 不定長 - 位置不定長， *args 號
def user_info4(*args):
    print(args) # 傳回元組('yoyo', '18')
user_info4("yoyo",'18')

# 不定長 - 位置不定長，　＊＊kwargs 號

def user_info5(**kwargs):
    print(kwargs) # 傳回字典{'name': 'yoyo', 'age': 18, 'id': 1}
user_info5(name="yoyo",age=18,id=1)