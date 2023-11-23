import sys

N = int(sys.stdin.readline())
str_list = []

for _ in range(N):
    str_list.append(sys.stdin.readline().strip())

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
        if len(left[i]) < len(right[j]):
            sorted_list.append(left[i])
            i += 1
        elif len(left[i]) == len(right[j]):
            if left[i] == right[j]:
                i += 1
            elif left[i] < right[j]:
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

for word in merge_sort(str_list):
    print(word)