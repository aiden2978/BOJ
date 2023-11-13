N = int(input())
cnt5 = 0

if N == 4 or N == 7:
    print(-1)
else:
    if N%5 == 0:
        print(int(N/5))
    elif N%5 == 1:
        print(int(N/5)+1)
    elif N%5 == 2:
        print(int(N/5)+2)
    elif N%5 == 3:
        print(int(N/5)+1)
    elif N%5 == 4:
        print(int(N/5)+2)
