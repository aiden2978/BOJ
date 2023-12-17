import sys

N = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split( )))
numlist_rev = numlist[::-1]

dp_max = [1 for _ in range(N)]
dp_min = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if numlist[i] > numlist[j]:
            dp_max[i] = max(dp_max[i], dp_max[j] + 1)
        if numlist_rev[i] > numlist_rev[j]:
            dp_min[i] = max(dp_min[i], dp_min[j] + 1)

maxvalue = 0
for i in range(N):
    if dp_max[i] + dp_min[N-1-i] > maxvalue:
        maxvalue = dp_max[i] + dp_min[N-1-i]

print(maxvalue - 1)