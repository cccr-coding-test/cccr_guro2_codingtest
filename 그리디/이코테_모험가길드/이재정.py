n = int(input())
arr = list(map(int, input().split()))
cnt = 0
i = 0

arr.sort(reverse=True)

while(True):
    if i < n:
        cnt += 1
        i += arr[i]
    else:
        break

print(cnt)
