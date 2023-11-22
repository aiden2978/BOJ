import sys

N = int(sys.stdin.readline())
ds_list = list(map(int, sys.stdin.readline().split( )))
el_list = list(map(int, sys.stdin.readline().split( )))
# qs_list = [[d, e] for d, e in zip(ds_list, el_list)]
M = int(sys.stdin.readline())
ins_list = list(map(int, sys.stdin.readline().split( )))
ret_list = []

for i in range(N):
    if ds_list[i] == 0:
        ret_list.append(el_list[i])
ret_list.reverse()
ret_list = ret_list + ins_list
print(*ret_list[:M])