import sys

N = int(sys.stdin.readline())
members = []

for _ in range(N):
    member = list(sys.stdin.readline().split( ))
    members.append([int(member[0]), member[1].strip()])

def merge_sort2(tosort_list):
    if len(tosort_list) <= 1:
        return tosort_list
    
    center = int(len(tosort_list)/2)
    left = tosort_list[:center]
    right = tosort_list[center:]

    return(merge(merge_sort2(left), merge_sort2(right)))

def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
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

for member in merge_sort2(members):
    print(*member)