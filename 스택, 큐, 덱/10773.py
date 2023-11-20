import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        stack.pop(len(stack)-1)

print(sum(stack))