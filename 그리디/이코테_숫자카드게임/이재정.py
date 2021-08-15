n, m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_val = min(arr)
    result = max(result, min_val)

print(result)

#sorting해서 첫 번째 인자를 list에 넣기
"""
result = []
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    result.append(arr[0])
    
print(max(result))
"""