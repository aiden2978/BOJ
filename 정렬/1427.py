N = int(input())
numlist = []

for i in range(len(str(N))):
    numlist.append(int(str(N)[i]))

numlist.sort(reverse = True)

print(*numlist, sep='')