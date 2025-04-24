student_scores = {
    "Tom": 85,
    "Alice": 92,
    "Bob": 78,
    "John": 60,
    "Lucy": 88,
    "Ken": 92,
    "Emma": 74
}
name = ""
mid_score = 0
max_score = max(student_scores.values()) # 最大數
min_score = min(student_scores.values()) # 最小數
# print(f"最高分:{max_score}")
# print(f"最低分:{min_score}")
for student in student_scores.keys():
    if student_scores[student] != max_score and student_scores[student] != min_score:
        mid_score = student_scores[student]
        name = student
print(f"中間分數的學生是 {name}，分數是 {mid_score}")