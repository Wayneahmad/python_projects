
print("Welcome to the average height calculator\n")
student_heights = input(
    "Input a list of student heights in cm - seperated by a space: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0

for height in student_heights:
    total_height += height
#print(str(total_height) + ("   = Total height"))

total_students = 0

for student in student_heights:
    total_students += 1
#print (f"{total_students}      = Total students")

average_height = round(total_height / total_students)
print(f"\n{average_height}  = Average height")
