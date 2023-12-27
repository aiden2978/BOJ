import sys

def BF(start):
    dist = [10001 for _ in range(N+1)]
    dist[start] = 0
    for i in range(N):
        for route in routes:
            [s, e, t] =  route
            if dist[s] + t < dist[e]:
                dist[e] = dist[s] + t
                if i == N - 1:
                    return False
    return True

T = int(sys.stdin.readline())

for _ in range(T):
    N, M, W = map(int, sys.stdin.readline().split( ))
    graph = [[10001 for _ in range(N+1)] for _ in range(N+1)]
    routes = []
    # hasNC = False

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split( ))
        if T < graph[S][E]:
            graph[S][E] = T
        if T < graph[E][S]:
            graph[E][S] = T

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split( ))
        if -T < graph[S][E]:
            graph[S][E] = -T

    for i in range(N+1):
        for j in range(N+1):
            if graph[i][j] < 10001:
                routes.append([i, j, graph[i][j]])

    # for i in range(1, N+1):
    #     if not BF(i):
    #         hasNC = True
    #         break
    
    # if hasNC:
    #     print("YES")
    # else:
    #     print("NO")
                
    if not BF(1):
        print("YES")
    else:
        print("NO")