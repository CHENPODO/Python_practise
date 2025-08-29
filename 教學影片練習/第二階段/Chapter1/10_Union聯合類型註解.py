# Union類型
# 導包
from typing import Union

my_list:list[Union[int,str]] = [1,2,"a","b"]

def func(data:Union[int,str]) -> Union[int,str]:
    pass

func() # 會提示 int | str
