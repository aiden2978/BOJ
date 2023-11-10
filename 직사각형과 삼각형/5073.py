while True:
    sides = list(map(int, input().split( )))
    sides.sort()

    if sides == [0, 0, 0]:
        break
    elif sides[0] + sides[1] <= sides[2]:
        print("Invalid")
    else:
        if sides[0] == sides[1] == sides[2]:
            print("Equilateral")
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            print("Isosceles")
        else:
            print("Scalene")