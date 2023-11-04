T = int(input())

for i in range(T):
    R, S = input().split( )
    R = int(R)

    strList = []
    resStr = ''
    for i in range(len(S)):
        strList.append(S[i])
        resStr += strList[i]*R
    print(resStr)

