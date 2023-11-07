N, B = input().split( )
B = int(B)
numList = []
BList = [str(i) for i in range(10)]
for i in range(26):
    BList.append(chr(i+65))

for i in range(len(N)):
    numList.append(N[i])

sum = 0
for i in range(len(numList)):
    sum += B**(len(numList)-1-i)*BList.index(numList[i])

print(sum)