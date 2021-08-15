N = int(input())
arr = list(map(int, input().split()))

arr[1] = max(arr[0], arr[1])
for i in range(2, N):
    arr[i] = max(arr[i-2]+arr[i], arr[i-1])
    # print(arr)

print(max(arr[N-1], arr[N-2]))