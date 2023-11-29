import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    clothes = {}
    cnt = 1
    for _ in range(n):
        a, b = sys.stdin.readline().strip().split( )
        if b in clothes:
            clothes[b] += 1
        else:
            clothes[b] = 1
    for v in clothes.values():
        cnt *= (v+1)
    print(cnt - 1)