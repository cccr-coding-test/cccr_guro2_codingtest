#답은 10이 꾸역꾸역 나오지만 풀이법도 다르고 어렵다..

n, m = map(int, input().split())
matrix = [[0]]*n

for i in range(n):
  matrix[i] = list(map(int, input()))

direct = [
  [1, 0],
  [0, 1],
  [1, 1]
]

cnt = 1

def bfs(y, x, cnt):

  if y == (n-1) and x == (m-1):
    print(cnt)

  for i in range(3):
    ny = y + direct[i][0]
    nx = x + direct[i][1]
    if ny < 0 or nx < 0 or ny >= n or nx >= m:
      continue
    
    if matrix[ny][nx] ==0:
      continue
    if matrix[ny][nx] == 1:
      cnt += 1
      bfs(ny, nx, cnt)


print(bfs(0, 0, cnt))



