a, b, c, d, e, f = map(int, input().split( ))
xans = 0
yans = 0

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            xans = x
            yans = y
        
print(xans, yans)