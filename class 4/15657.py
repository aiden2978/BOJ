import sys

N, M = map(int, sys.stdin.readline().split( ))
numlist = list(map(int, sys.stdin.readline().split( )))
numlist = sorted(numlist)


s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(0, N):
        if not s:
            s.append(numlist[i])
            dfs()
            s.pop()
        elif numlist[i] >= s[-1]:
            s.append(numlist[i])
            dfs()
            s.pop()

dfs()