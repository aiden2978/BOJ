numlist = []
for i in range(5):
    numlist.append(int(input()))

print(int(sum(numlist)/5))
print(sorted(numlist)[2])