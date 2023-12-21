import sys
from collections import deque

def find_nearest(pos):
    #  이동 가능한 칸까지 걸리는 시간 계산
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 상 좌 우 하
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    q = deque([pos])
    able = []

    while q:
        [curi, curj] = q.popleft()
        for k in range(4):
            newi = curi + dy[k]
            newj = curj + dx[k]
            # 격자 내의 칸이면서 아직 방문하지 않은 칸인지
            if 0 <= newi < N and 0 <= newj < N and not visited[newi][newj] and [newi, newj] != pos:
                # 이동 가능한 칸인지
                if space[newi][newj] <= shark[0]:
                    visited[newi][newj] = visited[curi][curj] + 1
                    q.append([newi, newj])
                    # 먹을 수 있는 물고기들을 able에 저장
                    if 0 < space[newi][newj] < shark[0]:
                        able.append([newi, newj])

    # able에 원소가 하나 이상일 때
    if able:
        for i in range(1, len(able)):
            # 거리가 최단거리가 아닌 원소들은 [20, 20]으로 바꾸어 정렬 시 최후순위로 보냄
            if visited[able[i][0]][able[i][1]] > visited[able[0][0]][able[0][1]]:
                able[i] = [20, 20]
        # 행, 열에 대해서 정렬
        able.sort(key = lambda x: (x[0], x[1]))
        # [걸린 시간, 좌표] 반환
        return [visited[able[0][0]][able[0][1]], able[0]]
    else:
        # 불가능
        return -1

N = int(sys.stdin.readline())
# [크기, 해당 크기에서 먹은 물고기 수]
shark = [2, 0]
# 1부터 6까지 각각의 크기를 갖는 물고기의 수
fish = [0 for _ in range(7)]
space = []
# 걸린 총 시간
cnt = 0

for i in range(N):
    line = list(map(int, sys.stdin.readline().split( )))
    for j in range(N):
        if 0 < line[j] <= 6:
            fish[line[j]] += 1
        elif line[j] == 9:
            # 현재 상어의 위치
            shark_pos = [i, j]
            line[j] = 0
    space.append(line)

# 먹을 수 있는 물고기가 남아있는지
# 즉 현재 크기보다 작은 물고기들의 개수의 합이 양수인지
while sum([fish[i] for i in range(min(shark[0], 7))]) > 0:
    # res = [걸린 시간, 이동한 좌표]
    res = find_nearest(shark_pos)
    # 더 이상 이동이 가능한지
    if res == -1:
        break
    else:
        cnt += res[0]
        # 기존에 상어가 있던 자리를 빈자리로 변환
        space[shark_pos[0]][shark_pos[1]] = 0
        # 상어가 새로 이동할 위치 저장
        shark_pos = res[1]
        # 상어가 이동하면서 먹힌 물고기의 크기
        eaten = space[shark_pos[0]][shark_pos[1]]
        fish[eaten] -= 1
        shark[1] += 1
        # 크기와 같은 수의 물고기를 먹었을 때 크기 +1
        if shark[1] == shark[0]:
            shark = [shark[0] + 1, 0]

print(cnt)