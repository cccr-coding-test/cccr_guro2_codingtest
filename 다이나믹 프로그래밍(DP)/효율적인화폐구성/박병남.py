n,m=map(int,input().split())
coins=[int(input()) for _ in range(n)]
canMake=[False]*(10001)

for coin in coins:
    canMake[coin]=1

for i in range(1,m+1):
    if canMake[i]:
        for coin in coins:
            if canMake[coin+i] is False:
                canMake[coin+i]=canMake[i]+1
            else:
                canMake[i+j]=min(canMake[i+j],canMake[i]+1)
print(canMake[m])
