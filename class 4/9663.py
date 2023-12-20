import sys
    
def dfs():
    global isAble, cnt
    if len(s) == N:
        cnt += 1
        return

    for i in range(N):
        if i not in s:
            if len(s) == 0:
                s.append(i)
                dfs()
                s.pop()
            else:
                isAble = True
                for j in range(len(s)):
                    if abs(len(s) - j) == abs(i - s[j]):
                        isAble = False
                        break
                if isAble:
                    s.append(i)
                    dfs()
                    s.pop()

N = int(sys.stdin.readline())

cnt = 0
isAble = True

s = []

dfs()
print(cnt)