# # range語法的練習案例:有幾個偶數
# # 定義一個變量 num ，內容隨意
# # 並使用range()語句，獲取從1到num的序列，使用for循環遍歷他，統計有多少偶數?
#
# num = 100
# count = 0
# for n in range(1,num):
#     if n % 2 ==0:
#         count += 1
# print(f"0~100中有{count }個偶數")

# # print(f"0~100中有{count - 1}個偶數") 有誤

# 🔢 請你印出從 1 到 100 所有偶數的「總和」是多少？
# （提示：可以用 if 判斷、或直接用步長為 2 的 range）
num = 100
count = 0
total = 0
for n in range(1, num + 1):  # 包含 100
    if n % 2 == 0:
        count += 1
        total += n

print(f"0~100中有{count}個偶數")
print(total)
