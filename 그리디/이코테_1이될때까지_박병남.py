n,k = map(int,input().split())
temp = (n//k) * k
count = n - temp
while True:
    if temp < k:
        break
    count += 1
    temp //= k

result = count + temp - 1
print(result)
