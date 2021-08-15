## 1이 될 때까지
# n, k = map(int, input().split())
# count = 0
# while n != 1:
#     if n % k == 0:
#         n /= k
#         count += 1
#     else:
#         n -= 1
#         count += 1  
# print(count)
# -- n 범위가 클 때 n을 1씩 빼면 시간 초과
n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k # K로 나누어 떨어지는 수
    result += (n - target) # target 까지 가기위해 1빼기 진행
    n = target
    if n < k:
        break # 못 나누는 경우 break
    result += 1 # 2번 연산 (나누기) 수행 한번 했으니 +1
    n //= k 

result -= 1 # 마지막 남은 수에 대하여 1씩 빼기
print(result)
