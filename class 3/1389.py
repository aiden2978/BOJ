import sys

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
        if left[i][1] < right[j][1]:
            sorted_list.append(left[i])
            i += 1
        elif left[i][1] == right[j][1]:
            if left[i][0] < right[j][0]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
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

N = int(sys.stdin.readline())
meetings = []

for _ in range(N):
    time = list(map(int, sys.stdin.readline().split( )))
    meetings.append(time)

meetings = merge_sort(meetings)

cnt = 0
start = 0

for i in range(N):
    if meetings[i][0] >= start:
        cnt += 1
        start = meetings[i][1]

print(cnt)