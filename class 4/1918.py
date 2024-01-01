import sys
from string import ascii_uppercase

input = sys.stdin.readline().strip()

num = []
op = []
brc_start = []

for i in range(len(input)):
    if input[i] == '(':
        brc_start.append(i)
    elif input[i] == ')':
        start = brc_start.pop()
        if not brc_start:
            num.append(input[start:i+1])

    if not brc_start:
        if input[i] in list(ascii_uppercase):
            num.append(input[i])
        elif input[i] in ['+', '-', '*', '/']:
            op.append(input[i])

print(num)
print(op)