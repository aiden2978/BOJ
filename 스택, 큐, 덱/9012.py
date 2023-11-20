import sys

def isVPS(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                return("NO")
            else:
                stack.pop()

    if len(stack) != 0:
        return("NO")
    else:
        return("YES")

N = int(sys.stdin.readline())
for _ in range(N):
    print(isVPS(sys.stdin.readline().strip()))