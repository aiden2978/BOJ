N, K = map(int, input().split( ))
divisor = []

for i in range(N):
    if N%(i+1) == 0:
        divisor.append(i+1)

if K > len(divisor):
    print(0)
else:
    print(divisor[K-1])