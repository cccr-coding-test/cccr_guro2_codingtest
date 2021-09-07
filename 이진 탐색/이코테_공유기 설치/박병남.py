n,c=map(int,input().split())
maps=list(int(input()) for _ in range(n))
maps.sort()

start=1
end=maps[-1]-maps[0]
result=0

while(start<=end):
    mid=(start+end)//2
    value=maps[0]
    count=1
    for i in range(1,n):
        if maps[i]>=value+mid:
            value=maps[i]
            count+=1
    if count>=c:
        start=mid+1
        result=mid
    else:
        end=mid-1

print(result)
