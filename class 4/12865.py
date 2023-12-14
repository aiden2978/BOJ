import sys

N, K = map(int, sys.stdin.readline().split( ))
items = []

for _ in range(N):
    items.append(list(map(int, sys.stdin.readline().split( ))))

# maxvalue[i][j]: i번째 물건까지 확인하였을 때 j의 용량 이내에서 최대 가치의 합
maxvalue = [[0 for _ in range(K+1)] for _ in range(N)]

if items[0][0] <= K:
    for i in range(items[0][0], K+1):
        maxvalue[0][i] = items[0][1]

for i in range(1, N):
    for j in range(1, K+1):
        if items[i][0] <= j:
            maxvalue[i][j] = max(maxvalue[i-1][j], maxvalue[i-1][j-items[i][0]] + items[i][1])
        else:
            maxvalue[i][j] = maxvalue[i-1][j]

print(maxvalue[N-1][K])