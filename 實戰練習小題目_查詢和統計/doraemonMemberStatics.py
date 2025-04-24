"""
一份多拉A夢角色的資料，每位角色有「職位」、「城市」、「年齡」三個欄位，
請你完成以下任務：

1. 找出所有住在「東京」的角色，並列出他們的名字與年齡。
2. 計算所有角色的平均年齡。
"""
from itertools import count

AllMember = {
    "大雄": {
        "職位": "學生",
        "城市": "東京",
        "年齡": 10
    },
    "靜香": {
        "職位": "學生",
        "城市": "東京",
        "年齡": 10
    },
    "胖虎": {
        "職位": "學生",
        "城市": "大阪",
        "年齡": 11
    },
    "小夫": {
        "職位": "學生",
        "城市": "東京",
        "年齡": 10
    },
    "哆啦A夢": {
        "職位": "機器貓",
        "城市": "22世紀未來",
        "年齡": 100
    }
}
# 1. 找出所有住在「東京」的角色，並列出他們的名字與年齡。
# 先定義一個東京組(字典)
tokyoTeams = {}
# 透過 for 迴圈跑判斷
for name in AllMember.keys(): # 遍歷出所有的 key 並附值給 name
    if AllMember[name]["城市"] == "東京": # 先判斷每一輪的城市是否等於東京
        tokyoTeams[name] = AllMember[name]["年齡"] # 將東京組每一輪的key = 全部成員[key][要找的Value值]

print(f"住在東京的角色與年齡如下：{tokyoTeams}")

# 2. 計算所有角色的平均年齡
AllMemberAge = 0 # 定義一個初始值
count = len(AllMember)
for age in AllMember.keys():
    AllMemberAge +=AllMember[age]["年齡"] # 每一輪都將年齡加上去給 AllMemberAge

average_age = AllMemberAge / count # 將迴圈跑完相加完成的年齡 / 總共多少人 = 平均
print(f"所有角色的平均年齡是{average_age:.1f}")