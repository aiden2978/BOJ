angles = []

for i in range(3):
    angles.append(int(input()))

angles.sort()

if angles[0] == angles[1] == angles[2] == 60:
    print('Equilateral')
elif sum(angles) == 180:
    if (angles[0] == angles[1]) or (angles[1] == angles[2]):
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')