import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(start, end):
    global proc
    q = deque([start])
    reg = [0 for _ in range(4)]
    ope = ['S', 'D', 'L', 'R']
    while q:
        cur = q.popleft()
        if cur == end:
            break
        reg[0] = (10000 + cur - 1) % 10000
        reg[1] = (2 * cur) % 10000
        reg[2] = (cur % 1000) * 10 + cur // 1000
        reg[3] = (cur % 10) * 1000 + cur // 10

        for i in range(4):
            if proc[reg[i]] == '':
                proc[reg[i]] = ''.join([proc[cur], ope[i]])
                q.append(reg[i])
            
    return(proc[end])

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split( ))
    proc = ['' for _ in range(10000)]
    print(bfs(A, B))