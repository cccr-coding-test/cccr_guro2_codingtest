from collections import deque

N, M = map(int, input().split())

g = []
for i in range(N):
    g.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 소스코드 구현
def bfs(x,y):
    # 큐 구현 위해 deque 라이브러리 사용
    q = deque()
    q.append((x,y))
    # 큐 빌 때까지 반복
    while q:
        x,y = q.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간 벗어난 경우 무시
            if nx <0 or ny<0 or nx >= N or nx >= M:
                continue
            # 벽인 경우 무시
            if g[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if g[nx][ny] == 1:
                g[nx][ny] = g[x][y] + 1
                q.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return g[N-1][M-1]

print(bfs(0,0))

# 책.. 참고...
# deque 라이브러리, popleft()