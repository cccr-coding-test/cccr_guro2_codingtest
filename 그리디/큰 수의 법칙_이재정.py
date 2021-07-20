N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
cycle_value = (K*arr[0])+arr[1]
result = int((( M/(K+1) )*cycle_value) + (( M % (K+1))*arr[0]))

print(result)

#단순 반복문을 사용한 방법
"""
arr = list(map(int, input().split()))
arr.sort(reverse=True)
sum = 0

for i in range(M):
    if i > 0 and i % K == 0:
        sum += arr[1]
    else:
        sum += arr[0]
"""
