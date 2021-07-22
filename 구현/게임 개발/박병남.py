# 맵 가장자리가 바다라는 조건을 못봄
# 단순 구현으로 풀어보기

def change_d(d):
    return 3 if d==0 else d-1

n,m=map(int,input().split())
x,y,d=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(m)]

# 바라보는 방향 :  북      동      남     서
 
# 가야하는 방향 :  서      북      동     남
d_list =     [[0,-1], [-1,0], [0,1], [1,0]]

maps[x][y]=-1 # 시작 위치 방문 처리  -1: 방문, 0: 미방문, 1: 바다
cnt=1 # 방문한 육지 카운트

while True:
    old_x,old_y=x,y
    
    for _ in range(4):
        dx,dy=d_list[d][0],d_list[d][1]
        nx,ny=x+dx,y+dy

        # 리스트 범위 밖일 때
        if nx<0 or ny<0 or n-1<nx or m-1<ny:
            d=change_d(d)
            continue

        # 미방문 육지일 때
        if maps[nx][ny]==0:
            maps[nx][ny]=-1
            cnt+=1
            x,y=nx,ny
            d=change_d(d)
            break

        # 주변에 갈곳이 없을 때 방향만 전환
        d=change_d(d)
    
    # 주변에 미방문 육지가 없을 때
    if old_x==x and old_y==y:

        if d==0: #북쪽 볼 때
            if x==m-1: #리스트 가장자리 라면
                break
            if maps[x+1][y]==1: #뒷쪽이 바다
                break
            x+=1 # 현재 좌표에서 뒤로 한 칸 이동

        if d==1: #동쪽 볼 때
            if y==0:
                break
            if maps[x][y-1]==1:
                break
            y-=1

        if d==2: #남쪽 볼 때
            if x==0:
                break
            if maps[x-1][y]==1:
                break
            x-=1

        if d==3: #서쪽 볼 때
            if y==m-1: 
                break
            if maps[x][y+1]==1:
                break
            y+=1

print(cnt)
