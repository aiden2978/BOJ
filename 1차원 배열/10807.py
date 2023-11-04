N = int(input())
numlist = list(map(int, input().split( )))
v = int(input())

count = 0
for i in range(N):
    if numlist[i] == v:
        count += 1

print(count)