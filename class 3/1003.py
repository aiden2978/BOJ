import sys
N = int(sys.stdin.readline())

def fib(n):
    a, b = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for _ in range(n-1):
            a, b = b, a+b
        return b
    
fib_list = [fib(i) for i in range(41)]
    
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        print(1, 0)
    else:
        print(fib_list[n-1], fib_list[n])