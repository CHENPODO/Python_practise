"""
練習題4：找出分數中間的學生

我們有一個學生的分數表，請你寫一段程式，找出「不是最高分也不是最低分」的學生，並印出他的名字與分數。

- 找出「不在最高分和最低分之間」的分數（也就是中間的分數）。

- 印出這個學生的名字和分數。

- 提示：

  - 找出最高分和最低分。

- 然後遍歷學生的分數，篩選出既不是最高分也不是最低分的學生。

- 只要有一個符合條件的學生，就印出來。
"""

student_scores = {
    "Tom": 85,
    "Alice": 92,
    "Bob": 78,
    "John": 60,
    "Lucy": 88,
    "Ken": 92,
    "Emma": 74

}

middle_score = 0  # 儲存中間分數
student_name = ""  # 儲存中間分數的學生名字

max_score = max(student_scores.values())  # 取得最高分
min_score = min(student_scores.values())  # 取得最低分

for student in student_scores.keys():
    # 如果這位學生的分數不是最高也不是最低，就代表是中間分數
    if student_scores[student] != max_score and student_scores[student] != min_score:
        student_name = student  # 記錄這位學生
        middle_score = student_scores[student]  # 記錄他的分數
        break  # 找到其中一位符合的就結束迴圈

print(f"中間成績是:{student_name},分數是:{middle_score}")
