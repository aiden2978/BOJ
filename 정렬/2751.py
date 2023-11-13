N = int(input())

numlist = [int(input())]

for i in range(1, N):
    numlist.append(int(input()))
    j = i
    while numlist[j] < numlist[j-1] and j >= 1:
        numlist[j-1], numlist[j] = numlist[j], numlist[j-1]
        j -= 1

for i in range(N):
    print(numlist[i])