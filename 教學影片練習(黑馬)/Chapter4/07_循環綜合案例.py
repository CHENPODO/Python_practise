# """
# 練習案例:發獎金
# 某公司，帳戶餘額1萬元，給20個員工發獎金
# """
# # 員工編號從1~20，每人可領1000元
# # 領獎金十，財務判斷績效(1~10) (隨機生成)，如低於5，不發獎金，下一位
# # 發完則結束
#
# """
# 提示:
# - 使用迴圈對員工發獎金
# - continue 用於跳過員工，break 直接結束
# - 隨機數可以用 random
# """
# import random
#
# money = 10000
# for member in range(1,21): # 員工 1 ~ 20
#     if money < 1000:
#         print("獎金全數發完!活動結束!")
#         break
#     score = random.randint(1,10) # 獨立評估
#
#     if score < 5:
#         print(f"員工編號為{member}，績效為{score}，不適用發獎金範圍")
#         continue
#
#     money -= 1000
#     print(f"獎金發送1000元，剩餘{money}元\n")
# print("發獎金結束")

# 無提示練習
import random

money = 5000
for member in range(1,21):
    print(f"本輪員工:{member}號!")
    if money < 1000:
        print("提早發完!")
        break
    score = random.randint(1,10)
    if score < 5:
        print(f"{member}號員工本次績校為: {score}，故不符合")
        continue
    money -= 1000
    print(f"發出獎金1000元，獎金剩餘:{money}")
print("全數頒發，下台一鞠躬")