
n,m=map(int,input().split())
mylist=[list(map(int,input().split())) for _ in range(n)]
result=0
for mlist in mylist:
    mlist.sort()
    result=max(result,mlist[0])
print(result)
