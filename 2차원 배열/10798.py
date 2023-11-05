words = []
for i in range(5):
    word = input()
    sublist = []
    for j in range(len(word)):
        sublist.append(word[j])
    words.append(sublist)

maxlen = 0
for sublist in words:
    if len(sublist) > maxlen:
        maxlen = len(sublist)

for sublist in words:
    while len(sublist) < maxlen:
        sublist.append(" ")

str = ''
for j in range(maxlen):
    for i in range(5):
        str += words[i][j]

resstr = str.replace(' ', '')
print(resstr)