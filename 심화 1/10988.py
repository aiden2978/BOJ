S = input()
a = int(len(S)/2)
result = 1

for i in range(a):
    if S[i] != S[len(S)-i-1]:
        result = 0

print(result)