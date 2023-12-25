import sys

N, M = map(int, sys.stdin.readline().split( ))
table = [list(map(int, sys.stdin.readline().split( ))) for _ in range(N)]
partial_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

partial_sum[0][0] = table[0][0]

for i in range(1, N):
    partial_sum[i][0] = 0
    partial_sum[0][i] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        partial_sum[i][j] = table[i-1][j-1] + partial_sum[i-1][j] + partial_sum[i][j-1] - partial_sum[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split( ))
    print(partial_sum[x2][y2] - partial_sum[x2][y1-1] - partial_sum[x1-1][y2] + partial_sum[x1-1][y1-1])