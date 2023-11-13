N = int(input())
counting = [0 for i in range(10001)]

for i in range(N):
    counting[int(input())] += 1

for i in range(10001):
    for j in range(counting[i]):
        print(i)