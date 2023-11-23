import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    proc = sys.stdin.readline().strip()
    if proc[:4] == 'push':
        stack.append(int(list(proc.split( ))[1]))
    elif proc == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            stackPop = stack.pop(len(stack)-1)
            print(stackPop)
    elif proc == 'size':
        print(len(stack))
    elif proc == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])