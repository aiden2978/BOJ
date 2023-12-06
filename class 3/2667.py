import sys

N = int(sys.stdin.readline())
graph = []
visited = [[0 for _ in range(N)] for _ in range(N)]
apt = []
cnt = 0
local_cnt = 1

for _ in range(N):
    lines_str = sys.stdin.readline().strip()
    lines = []
    for i in range(N):
        lines.append(int(lines_str[i]))
    graph.append(lines)

def dfs(x, y):
    global visited, local_cnt
    visited[x][y] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
            if not visited[x+dx[i]][y+dy[i]] and graph[x+dx[i]][y+dy[i]]:
                dfs(x+dx[i], y+dy[i])
                local_cnt += 1
    return local_cnt

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            apt.append(dfs(i, j))
            cnt += 1
            local_cnt = 1

apt = sorted(apt)
print(cnt)
for items in apt:
    print(items)