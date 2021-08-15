### solution 
n,k = map(int,input().split())
count = 0
while True:
    temp = (n//k) * k
    count = count + n - temp
    n = temp
    if n < k:
        break
    count += 1
    n //= k

result = count + n - 1
print(result)
