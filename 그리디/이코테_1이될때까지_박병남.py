### solution 1
n,k=map(int,input().split())
count = 0
while n>1:
    count += n%k
    temp = n//k
    if temp:
        n = temp
        count+=1
print(count)


### solution 2
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
