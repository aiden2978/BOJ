S = input()
crt2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
crt2Count = 0

for i in range(len(S)-1):
    if S[i:i+2] in crt2:
        crt2Count += 1


print(crt2Count)