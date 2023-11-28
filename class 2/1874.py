import sys

N = int(sys.stdin.readline())
isAble = True
rest = [i for i in range(N, 0, -1)]
stack = []
calc = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if stack != [] and num == stack[-1]:
        stack.pop()
        calc.append('-')
    elif num in rest:
        for j in range(rest[-1], num+1):
            a = rest.pop()
            stack.append(a)
            calc.append('+')
        stack.pop()
        calc.append('-')
    else:
        isAble = False
        break
    
if isAble == True:
    for char in calc:
        print(char)
else:
    print('NO')