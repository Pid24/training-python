fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits)

student_scores = [150, 142, 185, 120, 171, 184, 183, 180, 24, 59, 60, 89, 100, 69]
total_exam_scores = sum(student_scores)
print(total_exam_scores)

total_exam_scores = sum(student_scores)
sum = 0
for score in student_scores:
    sum += score
print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)