marks = [85, 92, 78, 90, 88]
total = 0
for mark in marks:
    total += mark
average = total / len(marks)
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print('Average:', average)
print('Grade:', grade)