"""
案例練習:數一數有幾個a

- 提示
1. 計數可以循環外定義一個整數類型變量作為累加計數
2. 判斷是否為字母 a ，可以通過 if 語句結合比較運算符
"""

name = "ithema is brand of itcast"

# 定義一個變量用來計算有幾個a
count = 0
# for 循環
for x in name:
    if x == 'a':
        count += 1
print(f"被統計的字符串中有{count}")
