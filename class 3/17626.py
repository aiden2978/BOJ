import sys
import math

N = int(sys.stdin.readline())

sq = [0 for _ in range(50001)]
for i in range(1, int(math.sqrt(N)) + 1):
    sq[i**2] = 1
sq[2] = 2
sq[3] = 3

for i in range(1, N+1):
    min = 4
    if sq[i] == 0:
        for j in range(1, int(math.sqrt(i)) + 1):
            if sq[i-j**2] + 1 < min:
                min = sq[i-j**2] + 1
        sq[i] = min

print(sq[N])