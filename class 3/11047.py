import sys

N, K = map(int, sys.stdin.readline().split( ))
cnt = 0

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

for i in reversed(range(N)):
    cnt += K//coins[i]
    K = K%coins[i]

print(cnt)