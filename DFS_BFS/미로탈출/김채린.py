from collections import deque

N, M = [int(x) for x in input().split()]
maze = []
for _ in range(N):
    maze.append([int(x) for x in input()])

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

# N, M = 5, 6
# maze = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [
#     0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]


def bfs(x, y):
    global N, M, maze

    q = deque()
    q.append((x, y))
    while q:
        curr = q.popleft()

        for d in direction:
            nx = curr[0] + d[0]
            ny = curr[1] + d[1]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:  # 다음 위치가 배열 범위를 넘어가지 않을 때
                if maze[nx][ny] == 0:  # 괴물이 있는 부분이면
                    pass
                elif maze[nx][ny] == 1:  # 아직 한 번도 안 간 곳이면
                    maze[nx][ny] = maze[curr[0]][curr[1]] + 1
                    q.append((nx, ny))
                else:  # 2보다 큰 때니까 한 번 이상 갔던 곳일 때
                    if maze[nx][ny] > maze[curr[0]][curr[1]] + 1:  # 한 번 갔었는데 지금 가면 더 빠르게 갈 수 있는 경우
                        maze[nx][ny] = maze[curr[0]][curr[1]] + 1
                        q.append((nx, ny))


bfs(0, 0)
print(maze[N-1][M-1])