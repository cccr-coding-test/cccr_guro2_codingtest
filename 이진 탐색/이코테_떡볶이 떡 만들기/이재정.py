n, m = map(int, input().split())

arr = list(map(int, input().split()))

def find(start, end):
    
    mid = (start + end)//2
    sum = 0
    for i in range(n):
        if arr[i] > mid:
            sum += (arr[i] - mid)
    if sum == m:
        print(mid)
        return
    if sum > m:
        find(mid+1, end)
    else:
        find(start, mid-1)

end = max(arr)
find(0, end)


