import bisect

N = 5
all_parts = [8, 3, 7, 9, 2]
all_parts.sort()

M = 3
orders = [5,7,9]

def binary_search(arr, x):
    i = bisect.bisect_left(arr, x)
    return i < len(arr) and arr[i] == x

for order in orders:
    if binary_search(all_parts, order):
        print('yes', end=" ")
    else:
        print('no', end=" ")

# 이진 탐색 구현

N = 5
all_parts = [8, 3, 7, 9, 2]
all_parts.sort()

M = 3
orders = [5,7,9]

def binary_search(arr, search):
    start, end = 0 , len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > search:
            end = mid -1
        elif arr[mid] < search:
            start = mid+1
        else:
            return mid
    return None

for order in orders:
    if binary_search(all_parts, order):
        print('yes', end=" ")
    else:
        print('no', end=" ")


# set 이용
N = 5
all_parts = [8, 3, 7, 9, 2]
# all_parts.sort()
all_parts = set(all_parts)

M = 3
orders = [5,7,9]

for order in orders:
    if order in all_parts:
        print('yes', end=" ")
    else:
        print('no', end=" ")