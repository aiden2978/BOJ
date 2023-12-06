import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = []
notblind = 0
blind = 0
red_cnt, green_cnt, blue_cnt, rg_cnt = 0, 0, 0, 0

for _ in range(N):
    lines_str = sys.stdin.readline().strip()
    lines = []
    for i in range(N):
        lines.append(lines_str[i])
    graph.append(lines)

def red_dfs(x, y):
    global visited
    if 0 <= x < N and 0 <= y < N:
        if graph[x][y] == 'R' and not visited[x][y]:
            visited[x][y] = 1
            red_dfs(x-1, y)
            red_dfs(x+1, y)
            red_dfs(x, y-1)
            red_dfs(x, y+1)
            return True
        else:
            return False
    else:
        return False
    
def green_dfs(x, y):
    global visited
    if 0 <= x < N and 0 <= y < N:
        if graph[x][y] == 'G' and not visited[x][y]:
            visited[x][y] = 1
            green_dfs(x-1, y)
            green_dfs(x+1, y)
            green_dfs(x, y-1)
            green_dfs(x, y+1)
            return True
        else:
            return False
    else:
        return False
    
def blue_dfs(x, y):
    global visited
    if 0 <= x < N and 0 <= y < N:
        if graph[x][y] == 'B' and not visited[x][y]:
            visited[x][y] = 1
            blue_dfs(x-1, y)
            blue_dfs(x+1, y)
            blue_dfs(x, y-1)
            blue_dfs(x, y+1)
            return True
        else:
            return False
    else:
        return False
    
def rg_dfs(x, y):
    global visited
    if 0 <= x < N and 0 <= y < N:
        if graph[x][y] != 'B' and not visited[x][y]:
            visited[x][y] = 1
            rg_dfs(x-1, y)
            rg_dfs(x+1, y)
            rg_dfs(x, y-1)
            rg_dfs(x, y+1)
            return True
        else:
            return False
    else:
        return False


visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if red_dfs(i, j):
            red_cnt += 1

visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if green_dfs(i, j):
            green_cnt += 1

visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if blue_dfs(i, j):
            blue_cnt += 1

visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if rg_dfs(i, j):
            rg_cnt += 1

print(red_cnt + green_cnt + blue_cnt, rg_cnt + blue_cnt)