# 소문자 ASCII: 97~

S = input()
res = [-1]*26
for i in range(0, 26):
    for j in range(len(S)):
        if chr(i+97) == S[j] and res[i] == -1:
            res[i] = j

resStr = ''
for i in res:
    resStr += str(i) + ' '

print(resStr)