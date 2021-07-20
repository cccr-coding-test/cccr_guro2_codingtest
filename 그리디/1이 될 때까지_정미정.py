# 입력 받은 수 n, 나눌 수 k

n,k = map(int, input().split())
count = 0

while n>1:
    if n%k==0:
        n= n//k
        count += 1
    else:
        n -= 1
        count += 1

print(count)