import collections

S = str(input())
partition = []

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        partition.append(S[i:j])

print(len(list(collections.Counter(partition).keys())))