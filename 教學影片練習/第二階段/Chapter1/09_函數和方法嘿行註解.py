# 對形參進行類型註解
def add(x:int,y:int):
    return x + y
add(1,2)
# 對覽回執進行類型註解
def func(data:list) -> list: # 最後回傳承list
    return  data

func(123) # 提示:但不會出錯
