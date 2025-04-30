"""
- 局部
- 全局
- global
"""
"""# 全局
num = "ok"
def testa():
    print(f"testa為:{num}")

def testb():
    print(f"testb為:{num}")

testa()
testb()
print(num)
"""

# 局部
"""def test_c():
    num = "ok"
    print(f"test_c:{num}")

def test_d():
    print(f"test_d:{num}")

test_c()
test_d()"""
"""
# global ，修改全局
num = "ok"
def test_c():
    print(f"test_c:{num}")

def test_d():
    num = "not ok!"
    print(f"test_d:{num}")

test_c()
test_d()
print(num)
"""

# 透過 global 關鍵字聲明全局變量
num = "ok"
def test_c():
    print(f"test_c:{num}")

def test_d():
    global num
    num = "not ok!"
    print(f"test_d:{num}")

test_c()
test_d()
print(num)
