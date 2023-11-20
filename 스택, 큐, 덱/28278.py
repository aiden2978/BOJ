import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    proc = sys.stdin.readline()
    if proc[0] == '1':
        stack.append(list(map(int, proc.split( )))[1])
    elif int(proc) == 2:
        if len(stack) == 0:
            print(-1)
        else:
            stackPop = stack.pop(len(stack)-1)
            print(stackPop)
    elif int(proc) == 3:
        print(len(stack))
    elif int(proc) == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])