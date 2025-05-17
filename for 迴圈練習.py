"""練習題目：
你現在有一個描述學生資訊的字典，每個學生有他的分數和班級。請你列出每位學生的名字、班級，並評價他們是否及格（60 分為及格線）。students = {
任務：
請你用 for 迴圈印出這樣的格式（每一行）：


小明（一甲）：85分，及格
小美（一乙）：58分，不及格
小強（一甲）：72分，及格
小華（一丙）：60分，及格
小英（一乙）：45分，不及格

for name, info in students.items():
    # name 是 "小明" 等等
    # info 是 {"score": ..., "class": ...}
"""
students ={
    "小明": {
        "score": 85,
        "class": "一甲"
    },
    "小美": {
        "score": 58,
        "class": "一乙"
    },
    "小強": {
        "score": 72,
        "class": "一甲"
    },
    "小華": {
        "score": 60,
        "class": "一丙"
    },
    "小英": {
        "score": 45,
        "class": "一乙"
    }
}

for name,info in students.items():
    """
    students -> 為一個字典
    .items() -> 一種方法，可以一次取得 key,value
    """
    score = info["score"]
    stu_class = info["class"]
    """
    上面的info是字典所以不可以使用 list or tuple
    """
    result = "及格" if score>= 60 else "不及格" # 三元運算式，如果結果為True 則result 則是 "及格"，否則皆為 "不及格"
    print(f"{name}( {stu_class} ):{score}分，{result}")