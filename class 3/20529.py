import sys

def dist2(A, B):
    cnt = 0
    for i in range(4):
        if A[i] != B[i]:
            cnt += 1
    return cnt

def dist3(A, B, C):
    return dist2(A, B) + dist2(B, C) + dist2(A, C)

T = int(sys.stdin.readline())

for _ in range(T):
    min_dist = 12
    N = int(sys.stdin.readline())
    MBTI = list(map(str, sys.stdin.readline().strip().split( )))

    if N >= 33:
        print(0)
    else:
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    if dist3(MBTI[i], MBTI[j], MBTI[k]) < min_dist:
                        min_dist = dist3(MBTI[i], MBTI[j], MBTI[k])
        
        print(min_dist)