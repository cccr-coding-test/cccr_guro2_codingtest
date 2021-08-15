#보통 큐(queue)는 선입선출(FIFO) 방식으로 작동한다. 반면, 양방향 큐가 있는데 그것이 바로 데크(deque)다.
# 즉, 앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.
# 데크는 양 끝 엘리먼트의 append와 pop이 압도적으로 빠르다.
# 컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우,
# 일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 데크(deque)는 O(1)로 접근 가능하다.

# 데크(deque), 언제, 왜 써야 하는가?
# 요약하자면, 데크(deque)는 스택처럼 사용할 수도 있고, 큐 처럼 사용할 수도 있다.
# 시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는 데 최적화된 연산 속도를 제공한다.
# 즉, 대부분의 경우에 데크(deque)는 리스트(list)보다 월등한 옵션이다.
# 데크는 특히 push/pop 연산이 빈번한 알고리즘에서 리스트보다 월등한 속도를 자랑한다.

from collections import deque
#크기
N, M = [int(x) for x in input().split()]
#맵생성
maze = []
for _ in range(N):
    maze.append([int(x) for x in input()])

#이동할 방향
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

# N, M = 5, 6
# maze = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [
#     0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]


def bfs(x, y):
    N, M, maze

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
                # else:  # 2보다 큰 때니까 한 번 이상 갔던 곳일 때
                #     if maze[nx][ny] > maze[curr[0]][curr[1]] + 1:  # 한 번 갔었는데 지금 가면 더 빠르게 갈 수 있는 경우
                #         maze[nx][ny] = maze[curr[0]][curr[1]] + 1
                #         q.append((nx, ny))


bfs(0, 0)
print(maze[N-1][M-1])