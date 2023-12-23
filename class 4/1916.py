import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    i, j, c = map(int, sys.stdin.readline().split( ))
    if graph[i][j] == -1:
        graph[i][j] = c
    else:
        graph[i][j] = min(graph[i][j], c)

start, end = map(int, sys.stdin.readline().split( ))

# start node까지의 비용은 0으로, 그 외 비용은 INF로 설정
distlist = [10**8+1 for _ in range(N+1)]
distlist[0], distlist[start] = 0, 0
visited = [0 for _ in range(N+1)]
visited[0] = 1
# (출발점으로부터 노드까지의 비용, 노드)를 heap에 저장
tovisit = [(0, start)]

# 더 이상 방문할 노드가 없을 때 까지
while tovisit:
    # 방문 가능한 노드 중 출발지로부터의 비용이 가장 적은 노드 호출
    (dist, node) = heapq.heappop(tovisit)
    for i in range(1, N+1):
        # 현재 노드로부터 갈 수 있는 노드들에 대해 최소비용 갱신
        if graph[node][i] >= 0:
            if distlist[node] + graph[node][i] < distlist[i]:
                distlist[i] = distlist[node] + graph[node][i]
            # 해당 노드가 아직 미방문 노드일 경우, 이후에 방문을 위해 heap에 push
                if not visited[i]:
                    heapq.heappush(tovisit, (distlist[i], i))
    # 방문처리
    visited[node] = 1

print(distlist[end])