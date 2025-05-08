"""
字符串相關工具
- 函數: str_reverse(s),接受傳入字符串,將字符串反轉返回
- 函數: substr(s,x,y),按照下標x和y,對字符串進行切片
"""

# def str_reverse(s):
#     lst = list(s)
#     lst.reverse()
#     return "".join(lst)
# print(str_reverse("abc"))

def str_reverse(s):
    return s[::-1] # start end step

def substr(s,x,y):
    return s[::1]

if __name__ == '__main__':
    print(substr("我愛你",0,3))