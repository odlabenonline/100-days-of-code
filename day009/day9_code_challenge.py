student_scores = {
    "Harry":    81,
    "Ron":      78,
    "Hermione": 99,
    "Draco":    74,
    "Neville":  62,
}
#Don't change the code above

#TODO-1: Create an empty dictionary called student_grade.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


#Don't change the code below
#print(student_scores, student_grades)
print(student_grades)

#91 100 Outstanding
#81  90 Exceeds Expectations
#71  80 Acceptable
#70 lower Fail