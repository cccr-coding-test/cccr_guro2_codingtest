# n*m 배열

n,m = map(int, input().split())
result = 0

for _ in range(n):
    a = list(map(int, input().split()))
    b = min(a)
    #li = [] li=li.append(b)

    result = max(result, b)

print(result)