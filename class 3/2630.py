import sys
import math
import numpy as np

N = int(sys.stdin.readline())
n = int(math.log2(N))

square = []
for _ in range(N):
    square.append(list(map(int,sys.stdin.readline().split( ))))


cnt_white = 0
def papers_white(list, r, c, d):
    divided_list = np.array(list)[r:r+d, c:c+d].tolist()
    print(divided_list)
    if len(divided_list) == 1:
        if divided_list == [0]:
            return 1
    elif set(sum(divided_list, [])) == {0}:
        return 1
    else:
        return papers_white(list, r, c, int(d/2)) + papers_white(list, r + int(d/2), c, int(d/2)) + papers_white(list, r, c + int(d/2), int(d/2)) + papers_white(list, r + int(d/2), c + int(d/2), int(d/2))
    
print(papers_white(square, 0, 0, N))