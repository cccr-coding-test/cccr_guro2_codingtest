from collections import deque

#n*n 크기 / k 가지의 바이러스
n,k=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
#s초 후 (result_x,result_y) 좌표 바이러스 종류는?
s,result_x,result_y=map(int,input().split())
#바이러스 초기위치 리스트
virus_start_locations=[]
steps=[[0]*n for _ in range(n)]
dx,dy=[1,-1,0,0],[0,0,-1,1]

for i in range(n):
    for j in range(n):
        if maps[i][j] != 0:
            virus_start_locations.append([i,j,maps[i][j]])
            steps[i][j]=1

def solution():
    global n,s,result_x,result_y
    queue=deque()
    for info in virus_start_locations:
        queue.append(info)
        flag=False
    while queue:
        if flag:
            break
        x,y,virus_kind=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or ny<0 or n<=nx or n<=ny:
                continue
            if maps[nx][ny]==0:
                steps[nx][ny]=steps[x][y]+1
                if steps[nx][ny]==s+2:
                    flag=True
                    break
                maps[nx][ny]=virus_kind
                queue.append([nx,ny,virus_kind])
            else:
                if steps[x][y]+1==steps[nx][ny]:
                    maps[nx][ny]=min(maps[nx][ny],virus_kind)
                    queue.append([nx,ny,virus_kind])
    return maps[result_x-1][result_y-1]

print(solution())
