import sys

uni = list(map(int, sys.stdin.readline().split( )))

print((uni[0]**2 + uni[1]**2 + uni[2]**2 + uni[3]**2 + uni[4]**2)%10)