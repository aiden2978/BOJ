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

        # [num, label] 형식으로 각각 최소 힙, 최대 힙에 삽입
        if proc == 'I':
            heapq.heappush(h_min, [num, i])
            heapq.heappush(h_max, [-num, i])
            cnt += 1
        else:
            # cnt (현재 이중 우선순위 큐 내에 있는 원소의 수)가 0보다 클 때만 작동
            if cnt > 0:
                cnt -= 1
                if num == 1:
                    # 최댓값을 pop했을 때, 아직 삭제되지 않은 숫자라면 deleted list에서 label index를 1로 바꿈
                    # 이미 삭제되었다면 (deleted[idx] == 1이라면), 그 다음 것을 pop
                    while True:
                        a = heapq.heappop(h_max)
                        if deleted[a[1]] == 0:
                            deleted[a[1]] = 1
                            break
                elif num == -1:
                    while True:
                        a = heapq.heappop(h_min)
                        if deleted[a[1]] == 0:
                            deleted[a[1]] = 1
                            break

    if cnt == 0:
        print('EMPTY')
    else:
        while h_max and deleted[h_max[0][1]]:
            heapq.heappop(h_max)

        while h_min and deleted[h_min[0][1]]:
            heapq.heappop(h_min)

        print(-h_max[0][0], h_min[0][0])