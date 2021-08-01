import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dducks = list(map(int, input().split()))

max_len = max(dducks)

answer = -1
start = 0
end = max_len
while start <= end:
    mid = (start+end)//2
    total_len = 0
    for dduck in dducks:
        total_len += dduck - mid if dduck > mid else 0
    if total_len < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
if answer == -1:
    print("can't")
else:
    print(answer)