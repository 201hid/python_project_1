student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


def grades(number):
    if number >= 91 and number <= 100:
        return "Outstanding"
    elif number >= 81 and number <= 90:
        return "Exceeds Expectations"
    elif number >= 71 and number <= 80:
        return "Acceptable"
    elif number <= 70:
        return "fail"


student_grades = {}

for i in student_scores:
    student_grades[i]=grades(student_scores[i])

print(student_grades)


