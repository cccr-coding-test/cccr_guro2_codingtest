from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

def count_by(array, left, right):
    right = bisect_right(array, right)
    left = bisect_left(array, left)
    return right - left

count = count_by(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)