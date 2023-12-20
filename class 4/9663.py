import sys
import itertools

def atk(q1, q2):
    if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return True
    else:
        return False

N = int(sys.stdin.readline())

nums = [i for i in range(N)]
combs = list(itertools.combinations(nums, 2))
cnt = 0
isAble = True

s = []

def dfs():
    global isAble, cnt
    if len(s) == N:
        isAble = True
        for comb in combs:
            if atk([comb[0], s[comb[0]]], [comb[1], s[comb[1]]]):
                isAble = False
                break
        if isAble:
            cnt += 1
        return
    
    for i in range(N):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
print(cnt)