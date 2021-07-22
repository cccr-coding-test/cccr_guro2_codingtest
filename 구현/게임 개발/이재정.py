import sys
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
matrix = []
visited = [[0]*m] * n

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for _ in range(n):
  row = list(map(int,sys.stdin.readline().rstrip().split()))
  matrix.append(row)

cnt = 0
move_cnt = 1
visited[x][y] = 1

while(True):
  
  direction -=1
  direction %= 4
  nx = x + dx[direction]
  ny = y + dy[direction]

  if visited[nx][ny] == 0 and matrix[nx][ny] == 0:
    visited[nx][ny] = 1
    x = nx
    y = ny
    cnt = 0
    move_cnt +=1
    continue
  else:
    cnt +=1
  
  if cnt == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if matrix[nx][ny] == 1:
      break
    else:
      x = nx
      y = ny
      cnt = 0

print(move_cnt)