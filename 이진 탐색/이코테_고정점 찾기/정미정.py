def fixed_point_search(array, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1
    
def solution(n, array):
    N = len(array)
    return fixed_point_search(array, start=0, end=N-1)
