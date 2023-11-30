import sys

N = int(sys.stdin.readline())

stairs = [0 for _ in range(301)]
for i in range(1, N+1):
    stairs[i] = int(sys.stdin.readline())

score = [0 for _ in range(301)]
score[1] = stairs[1]
score[2] = stairs[1] + stairs[2]
score[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, N+1):
    score[i] = max(score[i-2], score[i-3] + stairs[i-1]) + stairs[i]

print(score[N])