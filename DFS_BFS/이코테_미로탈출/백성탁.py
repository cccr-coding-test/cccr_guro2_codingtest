from collections import deque

N,M = map(int, input().split())

way = []
for _ in range(N):
    way.append(list(map(int,input())))

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))

#     while queue:
#         x,y = queue.popleft()

# 이건 더 어렵네요...
# 더 알아보겠습니다...
#--------------------------------------------------------
# 책 풀이

# 이동할 방향(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        # 현재 위치에서 4 방향으로 위치 확인 
        for i in range(4):
            nx = x + dx
            ny = y + dy

        # 미로 찾기 공간 벗어난 경우 무시
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        # 벽인 경우 무시
        if way[nx][ny] == 0:
            continue
        # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if way[nx][ny] ==1:
            way[nx][ny] == way[x][y] +1
            q.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return way[N-1][M-1]

print(bfs(0,0))

        