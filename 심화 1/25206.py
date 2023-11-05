grade = []
credit = []

for i in range(20):
    a, b, c = input().split( )
    if c != "P":
        credit.append(float(b))
        if c == "A+":
            grade.append(4.5)
        elif c == "A0":
            grade.append(4.0)
        elif c == "B+":
            grade.append(3.5)
        elif c == "B0":
            grade.append(3.0)
        elif c == "C+":
            grade.append(2.5)
        elif c == "C0":
            grade.append(2.0)
        elif c == "D+":
            grade.append(1.5)
        elif c == "D0":
            grade.append(1.0)
        elif c == "F":
            grade.append(0)

gradeTotal = 0
creditTotal = 0
for i in range(len(grade)):
    gradeTotal += grade[i]*credit[i]
    creditTotal += credit[i]

average = gradeTotal / creditTotal
print(average)