import sys
sys.setrecursionlimit(360000)

N, M = map(int, sys.stdin.readline().split( ))
campus = []
visited = [[0 for _ in range(M)] for _ in range(N)]
idx = [0, 0]
cnt = 0

for i in range(N):
    a = sys.stdin.readline().strip()
    subli = []
    for j in range(M):
        subli.append(a[j])
        if a[j] == 'I':
            idx = [i, j]
    campus.append(subli)

def dfs(x, y):
    global visited, cnt
    if 0 <= x < N and 0 <= y < M:
        if campus[x][y] != "X" and not visited[x][y]:
            visited[x][y] = 1
            if campus[x][y] == "P":
                cnt += 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

dfs(idx[0], idx[1])

if cnt != 0:
    print(cnt)
else:
    print("TT")