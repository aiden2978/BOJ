import sys

N, M = map(int, sys.stdin.readline().split( ))
numlist = list(map(int, sys.stdin.readline().split( )))
numlist = sorted(numlist)

reslist = []
s = []
idx = []

def dfs():
    if len(s) == M:
        a = ' '.join(map(str, s))
        if a not in reslist:
            reslist.append(a)
        return
    
    for i in range(0, N):
        if not idx:
            idx.append(i)
            s.append(numlist[i])
            dfs()
            idx.pop()
            s.pop()
        elif i >= idx[-1]:
            idx.append(i)
            s.append(numlist[i])
            dfs()
            idx.pop()
            s.pop()

dfs()

for a in reslist:
    print(a)