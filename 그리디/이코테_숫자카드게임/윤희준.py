N, M = map(int,input().split())
result =0
for i in range(N):
    n = list(map(int, input().split()))
    m = min(n) # 작은 수 찾기
    result = max(result, m) # 작은 수 중 큰 값 찾기
print(result)