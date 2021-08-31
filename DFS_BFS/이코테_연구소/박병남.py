from itertools import combinations
from copy import deepcopy
from collections import deque

n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
dx,dy=[1,-1,0,0],[0,0,1,-1]
zeros=list()
viruses=list()
safety_area=-3
for i,map in enumerate(maps):
    for j,ma in enumerate(map):
        if ma==0:
            zeros.append([i,j])
            safety_area+=1
        if ma==2:
            viruses.append([i,j])


def bfs(viruses):
    global n,m,safety_area
    queue=deque()
    virus_cnt=0
    for virus in viruses:
        queue.append(virus)
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or ny<0 or n<=nx or m<=ny:
                continue
            if my_maps[nx][ny]!=0:
                continue
            queue.append([nx,ny])
            my_maps[nx][ny]=2
            virus_cnt+=1
    return safety_area-virus_cnt
        
result=0

for blocking in combinations(zeros,3):
    my_maps=deepcopy(maps)
    for block in blocking:
        p,q=block
        my_maps[p][q]=1
    new=max(result,bfs(viruses))
    if result<new:
        result=new
        what=my_maps


print(result)
