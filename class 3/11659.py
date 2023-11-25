import sys

N, M = map(int, sys.stdin.readline().split( ))
arr = list(map(int, sys.stdin.readline().split( )))
arr_sum = [arr[0]]
for i in range(1, N):
    arr_sum.append(arr[i] + arr_sum[i-1])

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split( ))
    if a == 1:
        print(arr_sum[b-1])
    else:
        print(arr_sum[b-1] - arr_sum[a-2])