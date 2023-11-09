from collections import Counter

A = [0, 0, 0]
B = [0, 0, 0]
for i in range(3):
    A[i], B[i] = map(int, input().split( ))

print(Counter(A).most_common()[1][0], Counter(B).most_common()[1][0])