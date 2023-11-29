import sys

N, M = map(int, sys.stdin.readline().split( ))
trees = list(map(int, sys.stdin.readline().split( )))

start = 0
end = max(trees)

while start + 1 < end:
    mid = (start + end) // 2
    sum = 0
    for tree in trees:
        sum += max(tree - mid, 0)
    if sum < M:
        end = mid
    else:
        start = mid

print(start)