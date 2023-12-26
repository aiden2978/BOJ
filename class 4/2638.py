import sys
sys.setrecursionlimit(10**9)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# 외부의 공기인지 check하여 외부이면 -1로 바꿈
def check_outer(i, j):
    graph[i][j] = -1
    for k in range(4):
        if 0 <= i + di[k] < N and 0 <= j + dj[k] < M:
            if graph[i + di[k]][j + dj[k]] == 0:
                check_outer(i + di[k], j + dj[k])

# 외부의 공기와 2면 이상 닿아있다면 True 반환
def tomelt(i, j):
    local_cnt = 0
    for k in range(4):
        if 0 <= i + di[k] < N and 0 <= j + dj[k] < M:
            if graph[i + di[k]][j + dj[k]] == -1:
                local_cnt += 1
    if local_cnt >= 2:
        return True
    else:
        return False

N, M = map(int, sys.stdin.readline().split( ))
graph = []
cnt = 0
time = 0

for i in range(N):
    lines = list(map(int, sys.stdin.readline().split( )))
    graph.append(lines)
    for j in range(M):
        if lines[j] == 1:
            cnt += 1

# 가장자리로부터 외부 공기인지 초기 확인
for i in range(N):
    if graph[i][0] == 0:
        check_outer(i, 0)
    if graph[i][M-1] == 0:
        check_outer(i, M-1)

for j in range(1, M - 1):
    if graph[0][j] == 0:
        check_outer(0, j)
    if graph[N-1][j] == 0:
        check_outer(N-1, j)

while cnt > 0:
    tomelt_list = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if tomelt(i, j):
                    tomelt_list.append([i, j])
                    cnt -= 1

    # 이번에 녹는 점들을 모두 모아 한번에 전환
    for item in tomelt_list:
        graph[item[0]][item[1]] = -1

    # 녹으면서 생기는 새로운 외부 공기 칸들로부터 이어진 외부공기 확인
    for item in tomelt_list:
        check_outer(item[0], item[1])

    time += 1

print(time)