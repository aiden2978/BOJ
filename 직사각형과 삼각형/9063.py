N = int(input())
A = [0 for i in range(N)]
B = [0 for i in range(N)]

for i in range(N):
    A[i], B[i] = map(int, input().split( ))

print((max(A)-min(A))*(max(B)-min(B)))