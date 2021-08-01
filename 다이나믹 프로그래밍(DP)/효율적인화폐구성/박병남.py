n,m=map(int,input().split())
coins=[int(input()) for _ in range(n)]
d=[-1]*(10001)

for coin in coins:
    d[coin]=1

for i in range(1,m+1):
    if d[i]!=-1:
        for coin in coins:
            if d[coin+i]==-1:
                d[coin+i]=d[i]+1
            else:
                d[i+j]=min(d[i+j],d[i]+1)
print(d[m])
