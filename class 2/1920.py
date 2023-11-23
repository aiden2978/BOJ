import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split( )))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split( )))

def binary_search(target, sorted_list, left, right):
    result = False
    center = int((left + right)/2)
    while right - left > 0:
        if sorted_list[center] == target:
            result = True
            break
        elif sorted_list[center] > target:
            return(binary_search(target, sorted_list, left, center-1))
        else:
            return(binary_search(target, sorted_list, center+1, right))
    if left == right:
        if sorted_list[center] == target:
            result = True
    return result

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

sorted_A = merge_sort(A)

for i in range(M):
    if binary_search(B[i], sorted_A, 0, N-1):
        print(1)
    else:
        print(0)