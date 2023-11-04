# 대문자 아스키 65~

S = input()
sum = 0

for i in range(len(S)):
    n = ord(S[i])
    if n <= 67:
        sum += 3
    elif n <= 70:
        sum += 4
    elif n <= 73:
        sum += 5
    elif n <= 76:
        sum += 6
    elif n <= 79:
        sum += 7
    elif n <= 83:
        sum += 8
    elif n <= 86:
        sum += 9
    elif n <= 90:
        sum += 10

print(sum)