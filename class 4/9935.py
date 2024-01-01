import sys

def check(i):
    if ''.join(stack[i-len_bomb:]) == bomb:
        for _ in range(len_bomb):
            stack.pop()

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
len_bomb = len(bomb)

stack = []

for i in range(len(string)):
    stack.append(string[i])
    if len(stack) >= len_bomb:
        check(len(stack))

if stack:
    print(*stack, sep = '')
else:
    print("FRULA")