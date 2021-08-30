N = int(input())
array = list(map(int, input().split()))

def binary_search(array,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return False

result = binary_search(array, 0, N-1)
if result == False:
    print(-1)
else:
    print(result)