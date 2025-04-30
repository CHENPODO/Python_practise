"""# 會分行輸出
print("Hello")
print("World")

# 加上 ,end = '' ，則會不換行
print("Hello",end="")
print("World",end="")
"""
# 特殊符號 \t 會對齊
# 不會對齊
"""
Hello World
itheima best
"""
print("Hello World")
print("itheima best")
# 特殊符號 \t 會對齊
"""
Hello	World
itheima	best
"""
print("Hello\tWorld")
print("itheima\tbest")