
## 숫자 카드 게임
n, m = map(int, input().split())
result = 0
for i in range(n):
    row = list(map(int, input().split()))
    row_min = min(row)
    result = max(result, row_min)
print(result)


