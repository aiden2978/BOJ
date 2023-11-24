import sys
T = int(sys.stdin.readline())

sum_list = [0 for _ in range(11)]

for i in range(1, 11):
    if i == 1:
        sum_list[i] = 1
    elif i == 2:
        sum_list[i] = 2
    elif i == 3:
        sum_list[i] = 4
    else:
        sum_list[i] = sum_list[i-1] + sum_list[i-2] + sum_list[i-3]

for _ in range(T):
    N = int(sys.stdin.readline())
    print(sum_list[N])