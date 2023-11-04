students = []
for i in range(1, 31):
    students.append(i)

for i in range(28):
    num = int(input())
    students.remove(num)

print(students[0])
print(students[1])
