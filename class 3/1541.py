import sys
import re

exp = sys.stdin.readline().strip()
numbers = re.findall(r'\d+', exp)
sign = []
for i in range(len(exp)):
    if exp[i] == '+' or exp[i] == '-':
        sign.append(exp[i])

if set(sign) == {'+'}:
    sum = 0
    for i in range(len(numbers)):
        sum += int(numbers[i])
    print(sum)

else:
    sum = int(numbers[0])
    for i in range(len(sign)):
        if sign[i] == '+':
            sum += int(numbers[i+1])
        else:
            for j in range(i, len(sign)):
                sum -= int(numbers[j+1])
            break

    print(sum)