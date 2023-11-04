S = input()
S = S.strip()
count = 1

if len(S) == 0:
    count = 0
else:
    for i in range(len(S)):
        if S[i] == ' ':
            count += 1

print(count)
