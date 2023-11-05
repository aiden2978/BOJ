background = [[0 for i in range(100)] for i in range(100)]

N = int(input())
for i in range(N):
    a, b = map(int, input().split( ))

    for j in range(10):
        for k in range(10):
            background[a+j-1][b+k-1] = 1

sum = 0
for i in range(100):
    for j in range(100):
        sum += background[i][j]

print(sum)


