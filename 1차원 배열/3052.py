remList = []
for i in range(10):
    num = int(input())%42
    if num not in remList:
        remList.append(num)

print(len(remList))