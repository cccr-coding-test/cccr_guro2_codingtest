n=int(input())
mylist=[list(map(int,input().split())) for _ in range(n)]
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            left=0
        else:
            left=mylist[i-1][j-1]
        if j==i:
            right=0
        else:
            right=mylist[i-1][j]
        mylist[i][j]=max(mylist[i][j]+left,mylist[i][j]+right)

print(max(mylist[-1]))
