N = int(input())
groupCount = 0

for i in range(N):
    word = input()
    wordList = []
    for j in range(len(word)):
        wordList.append(word[j])
    
    for j in range(len(word)-1):
        if wordList[j] == wordList[j+1]:
            wordList[j] = 0

    while 0 in wordList:
        wordList.remove(0)

    if len(wordList) == len(set(wordList)):
        groupCount += 1

print(groupCount)