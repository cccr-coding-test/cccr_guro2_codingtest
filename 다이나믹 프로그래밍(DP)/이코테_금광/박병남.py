testCase=int(input())
for _ in range(testCase):
    n,m=map(int,input().split())
    
    mylist=list(map(int,input().split()))
    goldlist=[[] for _ in range(m)]
    for i,my in enumerate(mylist):
        goldlist[i%m].append(my)
    
    for j in range(1,m):
        for i in range(n):
            left=goldlist[j-1][i]
            if i==0:
                left_up=0
            else:
                left_up=goldlist[j-1][i-1]
            if i==n-1:
                left_down=0
            else:
                left_down=goldlist[j-1][i+1]
            goldlist[j][i]=goldlist[j][i]+max(left,left_down,left_up)

    print(max(goldlist[m-1]))
