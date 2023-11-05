word = input().upper()
alpCount = [0]*26

for i in range(len(word)):
    index = ord(word[i])-65
    alpCount[index] += 1

if sorted(alpCount, reverse=True)[0] == sorted(alpCount, reverse=True)[1]:
    print("?")
else:
    maxIndex = alpCount.index(max(alpCount))
    print(chr(maxIndex+65))

