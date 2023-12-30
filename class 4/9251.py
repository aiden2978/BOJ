import sys

firststr = sys.stdin.readline().strip()
secondstr = sys.stdin.readline().strip()

lcs = [[0 for _ in range(len(secondstr)+1)] for _ in range(len(firststr)+1)]

for i in range(len(firststr)):
    for j in range(len(secondstr)):
        if firststr[i] == secondstr[j]:
            lcs[i+1][j+1] = lcs[i][j] + 1
        else: # 하나씩 추가했을 때를 비교
            lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])

print(lcs[-1][-1])