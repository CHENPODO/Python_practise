# for i in range(0,2):
#     print("語句1")
#     continue
#     print("語句2") #不會執行該行

# for 嵌套
# for i in range(0,1):
#     print("語句1")
#     for i in range(0,1):
#         print("語句2")
#         continue
#         print("語句3") #不會執行該行
#     print("語句4")
#

# for i in range(0,3): # 只要遇到 break 迴圈會強制停止!不會管你要執行幾次
#     print("語句1")
#     break
#     print("語句2")
# print("語句3")

# for 嵌套
for i in range(1, 6):
    print("語句1")
    for j in range(1, 6):  # 改為 j
        print("語句2")
        break
        print("語句3")  # 不會執行該行
    print("語句4")
