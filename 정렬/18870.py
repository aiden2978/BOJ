import sys

N = int(sys.stdin.readline())
points = list(map(int, sys.stdin.readline().split( )))
comp_points = []

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
        elif left[i] == right[j]:
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

sorted_points = merge_sort(points)

# 이분 탐색: 정렬된 list에 대하여 중간값이 target 보다 크면 왼쪽 분할 list 탐색, 작으면 오른쪽 분할 list 탐색
def binary_search(target, sorted_list, left, right):
    center = int((left + right)/2)
    while sorted_list[center] != target:
        if sorted_list[center] > target:
            return(binary_search(target, sorted_list, left, center-1))
        else:
            return(binary_search(target, sorted_list, center+1, right))
    return center

for point in points:
    comp_points.append(binary_search(point, sorted_points, 0, len(sorted_points)-1))

print(*comp_points)