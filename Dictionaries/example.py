students_score = {
    "Harry": 98,
    "Will": 76,
    "Sharon": 85,
    "Jane": 60
}

student_grade = {}

for key in students_score:
    if students_score[key] > 90:
        student_grade[key] = "Outstanding"
    elif students_score[key] > 80:
        student_grade[key] = "Excellent"
    elif students_score[key] > 70:
        student_grade[key] = "Expectation"
    else:
        student_grade[key] = "Fail"
print(student_grade)