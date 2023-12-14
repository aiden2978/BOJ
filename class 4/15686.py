import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split( ))

graph = []
houses = []
stores = []
chickens = []

for i in range(N):
    lines = list(map(int, sys.stdin.readline().split( )))
    graph.append(lines)
    for j in range(N):
        if lines[j] == 1:
            houses.append([i, j])
        if lines[j] == 2:
            stores.append([i, j])

for house in houses:
    dist = []
    for store in stores:
        dist.append(abs(store[1] - house[1]) + abs(store[0] - house[0]))
    chickens.append(dist)

nums = [i for i in range(len(stores))]
combs = list(combinations(nums, M))

global_min = 10**9

for comb in combs:
    sum = 0
    for dist in chickens:
        local_min = 10**9
        for i in range(M):
            if dist[comb[i]] < local_min:
                local_min = dist[comb[i]]
        sum += local_min
    if sum < global_min:
        global_min = sum

print(global_min)