import sys

N = int(sys.stdin.readline())
diff = []
for _ in range(N):
    diff.append(int(sys.stdin.readline()))

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

# round() 함수는 2.5 등의 경우 가까운 짝수를 반환 -> 매우 작은 상수를 더해 해결
if N == 0:
    print(0)
else:
    ig = round(N*0.15 + 0.00000001)
    diff = merge_sort(diff)[ig : N-ig]

    print(round(sum(diff)/(N-2*ig) + 0.00000001))