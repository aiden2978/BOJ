import sys

N = int(sys.stdin.readline())
paint = []

for _ in range(N):
    cost = list(map(int, sys.stdin.readline().split( )))
    paint.append(cost)

min_r = [paint[0][0]]
min_g = [paint[0][1]]
min_b = [paint[0][2]]

for i in range(1, N):
    min_r.append(min(min_g[i-1], min_b[i-1]) + paint[i][0])
    min_g.append(min(min_b[i-1], min_r[i-1]) + paint[i][1])
    min_b.append(min(min_r[i-1], min_g[i-1]) + paint[i][2])

print(min(min_r[N-1], min_g[N-1], min_b[N-1]))