import sys
N = int(sys.stdin.readline())
one_list = [0 for _ in range(1000001)]

for i in range(2, N+1):
    if i%6 == 0:
        one_list[i] = min(one_list[int(i/3)], one_list[int(i/2)], one_list[i-1]) + 1
    elif i%3 == 0:
        one_list[i] = min(one_list[int(i/3)], one_list[i-1]) + 1
    elif i%2 == 0:
        one_list[i] = min(one_list[int(i/2)], one_list[i-1]) + 1
    else:
        one_list[i] =  one_list[i-1] + 1

print(one_list[N])