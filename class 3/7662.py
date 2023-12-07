import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    h_min = []
    h_max = []
    cnt = 0

    k = int(sys.stdin.readline())
    deleted = [0 for _ in range(k)]

    for i in range(k):
        proc, num = map(str, sys.stdin.readline().strip().split( ))
        num = int(num)

        if proc == 'I':
            heapq.heappush(h_min, [num, i])
            heapq.heappush(h_max, [-num, i])
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
                if num == 1:
                    a = heapq.heappop(h_max)
                    deleted[a[1]] = 1
                    print(deleted)
                elif num == -1:
                    a = heapq.heappop(h_min)
                    deleted[a[1]] = 1
                    print(deleted)

    if cnt == 0:
        print('EMPTY')
    else:
        i = 0
        while True:
            if not deleted[h_max[i][1]]:
                M = -deleted[h_max[i][0]]
                break
            i += 1

        i = 0
        while True:
            if not deleted[h_min[i][1]]:
                m = deleted[h_min[i][0]]
                break
            i += 1

        print(M, m)