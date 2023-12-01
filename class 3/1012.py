import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global visited
    # 범위를 벗어난 점들에 대해서는 False
    if 0 <= x < N and 0 <= y < M:
    # 그래프 상 1이고 아직 방문하지 않은 점들에 대해서는 방문한 점으로 처리하고, 인접한 점들에 대해서도 동일한 시행을 반복
    # 이후 True를 반환함으로써 모임에 속한 한 점을 함수에 대입하면 모임 유무를 반환하고 모임에 속한 모든 점들이 방문 처리가 된다.
        if graph[x][y] and not visited[x][y]:
            visited[x][y] = 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        else:
            return False
    else:
        return False

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split( ))
    
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split( ))
        graph[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                cnt += 1

    print(cnt)