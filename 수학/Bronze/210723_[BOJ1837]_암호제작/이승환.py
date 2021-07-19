# 에라토스테네스의 체
# 1부터 n까지의 숫자를 쓰고 1을 제거
# 2를 제외한 2의 배수를 제거
# 3을 제외한 3의 배수를 제거
# 5를 제외한 5의 배수를 제거
# 7을 제외한 7의 배수를 제거
# n = int(input())
a = [False, False] + [True] * (n - 1)   # 1은 소수가 아니고 인덱스가 수를 의미하기 위해 원소는 n + 1개
primes=[]                               # 소수 모음
for i in range(2, int(n ** 0.5) + 1):   # 2부터 n의 제곱근까지
  if a[i]:                              # i가 소수이면(True) 소수 모음에 추가
    primes.append(i)
    for j in range(2 * i, n + 1, i):    # i를 제외한 2 * i부터 모든 배수 지움
        a[j] = False
# print(primes)

# 풀이에 적용
P, K = map(int, input().split())

a = [False, False] + [True] * (K - 1)
prime = []
for i in range(2, K + 1):
    if a[i]:
        prime.append(i)
        for j in range(2 * i, K + 1, i):
            a[j] = False

result = 'GOOD'
for item in prime:              # K보다 작은 소수들 중
    if P % item == 0:           # 나누어 떨어지면 반복문 종료
        result = f'BAD {item}'
        break
print(result)