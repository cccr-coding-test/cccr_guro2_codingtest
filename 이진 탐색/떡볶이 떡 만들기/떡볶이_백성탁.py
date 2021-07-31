N, M = map(int, input().split())
heights = list(map(int, input().split()))

low, high = 0, max(heights)

result = 0


while low <= high:
    total = 0
    middle = (low + high) // 2

    for i in heights:
        if i > middle:
            total += (i - middle)

    if total < M:
        high = middle - 1
    else:
        result = middle
        low = middle + 1

print(result)
