import sys
import math
from collections import Counter

N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

def merge_sort(tosort_list):
    if len(tosort_list) <= 1:
        return tosort_list
    
    center = int(len(tosort_list)/2)
    left = tosort_list[:center]
    right = tosort_list[center:]

    return(merge(merge_sort(left), merge_sort(right)))

def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list

numbers = merge_sort(numbers)

print(round(sum(numbers)/N))
print(numbers[N//2])
numbers_c = Counter(numbers)
numbers_common = numbers_c.most_common(2)
if N == 1:
    print(numbers[0])
else:
    if numbers_common[0][1] != numbers_common[1][1]:
        print(numbers_common[0][0])
    else:
        print(numbers_common[1][0])
if N == 1:
    print(0)
else:
    print(numbers[N-1] - numbers[0])