import sys
import heapq

N, E= map(int, sys.stdin.readline().split( ))
start = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

# 인접 행렬의 경우 4억 개 이상의 원소가 필요하므로 메모리를 줄이기 위해 인접 리스트 이용
for _ in range(E):
    i, j, c = map(int, sys.stdin.readline().split( ))
    graph[i].append([j, c])

# start node까지의 비용은 0으로, 그 외 비용은 INF로 설정
distlist = [10**6+1 for _ in range(N+1)]
distlist[0], distlist[start] = 0, 0
visited = [0 for _ in range(N+1)]
visited[0] = 1
# (출발점으로부터 노드까지의 비용, 노드)를 heap에 저장
tovisit = [(0, start)]

# 더 이상 방문할 노드가 없을 때 까지
while tovisit:
    # 방문 가능한 노드 중 출발지로부터의 비용이 가장 적은 노드 호출
    (dist, node) = heapq.heappop(tovisit)
    for line in graph[node]:
        if distlist[line[0]] > distlist[node] + line[1]:
            distlist[line[0]] = distlist[node] + line[1]
            if not visited[line[0]]:
                heapq.heappush(tovisit, (distlist[line[0]], line[0]))

    visited[node] = 1

for i in range(1, N+1):
    if distlist[i] == 10**6 + 1:
        print('INF')
    else:
        print(distlist[i])