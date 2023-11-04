N, X = map(int, input().split( ))
A = list(map(int, input().split( )))
newlist = []

for i in range(N):
    if A[i] < X:
        newlist.append(A[i])
newlistTostring = ' '.join(str(s) for s in newlist)

print(newlistTostring)