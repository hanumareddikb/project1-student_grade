student_name = input("Enter student name: ")
pointspossible = float(input("Enter total marks: "))
score = float(input("Enter student score: "))

student_percentage = (score/pointspossible)*100

if student_percentage >= 90:
    Grade = "A"
elif student_percentage >= 80:
    Grade = "B"
elif student_percentage >= 70:
    Grade = "C"
elif student_percentage >= 60:
    Grade = "D"
else:
    Grade = "F"
    j

print(f"Student Name is {student_name} and Grade obtained is {Grade}")
