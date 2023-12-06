import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

alt = [0 for _ in range(M)]
cnt = 0
for i in range(1, M):
    if S[i] != S[i-1]:
        alt[i] = alt[i-1] + 1
    else:
        alt[i] = 0
    if i >= 2*N and S[i - 2*N] == "I" and alt[i] >= 2*N:
        cnt += 1

print(cnt)