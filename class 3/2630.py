import sys

N = int(sys.stdin.readline())

square = []
for _ in range(N):
    square.append(list(map(int,sys.stdin.readline().split( ))))


cnt_white = 0
cnt_blue = 0
def papers(list, r, c, d):
    global cnt_white, cnt_blue
    divided_list = [row[r:r+d] for row in list[c:c+d]]
    if set(sum(divided_list, [])) == {0}:
        cnt_white += 1
    elif set(sum(divided_list, [])) == {1}:
        cnt_blue += 1
    else:
        papers(list, r, c, int(d/2))
        papers(list, r + int(d/2), c, int(d/2))
        papers(list, r, c + int(d/2), int(d/2))
        papers(list, r + int(d/2), c + int(d/2), int(d/2))
    
papers(square, 0, 0, N)
print(cnt_white)
print(cnt_blue)