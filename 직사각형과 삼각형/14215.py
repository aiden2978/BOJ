sides = list(map(int, input().split( )))
sides.sort()
sides[2] = min(sides[2], sides[0] + sides[1] - 1)

print(sum(sides))