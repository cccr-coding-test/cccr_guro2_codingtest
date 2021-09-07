def solution(N, stages):
    answer = []
    mylist=[[i,0] for i in range(1,N+1)]
    clearlist=[0]*(N+1)
    faillist=[0]*(N+1)
    for stage in stages:
        if stage==N+1:
            clearlist[N-stage+1]+=1
            continue
        clearlist[N-stage+1]+=1
        faillist[stage]+=1
    for i in range(1,N+1):
        fail=faillist[i]
        clear=sum(clearlist[:N-i+2])
        if clear !=0:
            mylist[i-1][1]=fail/clear
    mylist.sort(key=lambda x:x[1],reverse=True)
    answer=[]
    for my in mylist:
        answer.append(my[0])
    return answer



N=int(input())
stages=list(map(int,input().split()))
print(solution(N,stages))
