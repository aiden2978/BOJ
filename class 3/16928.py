import sys
from collections import deque
sys.setrecursionlimit(10000)

board = [0 for _ in range(101)]
updown = [0 for _ in range(101)]

N, M = map(int, sys.stdin.readline().split( ))

for _ in range(N + M):
    a, b = map(int, sys.stdin.readline().split( ))
    updown[a] = b

q = deque([1])
while q:
    cur = q.popleft()
    for i in range(1, 7):
        num = cur + i
        if num <= 100:
            if not board[num]:
                if not updown[num]:
                    board[num] = board[cur] + 1
                    q.append(num)
                else:
                    togo = updown[num]
                    if not board[togo]:
                        board[togo] = board[cur] + 1
                        q.append(togo)

print(board[100])