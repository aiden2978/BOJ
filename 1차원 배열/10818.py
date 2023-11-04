N = int(input())
numlist = list(map(int, input().split( )))

max = numlist[0]
min = numlist[0]

for i in numlist:
    if i > max:
        max = i
    if i < min:
        min = i
    
print(min, max)