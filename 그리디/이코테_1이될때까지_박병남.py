n,k=map(int,input().split())
count = 0
while n>1:
    count += n%k
    temp = n//k
    if temp:
        n = temp
        count+=1
print(count)
