import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

cnt = 0
PN = 'I'
for _ in range(N):
    PN += 'OI'

for i in range(M-2*N):
    if S[i:i+(2*N+1)] == PN:
        cnt += 1

print(cnt)