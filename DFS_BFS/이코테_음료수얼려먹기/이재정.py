n, m = map(int, input().split())

matrix = [[0]]*n
result = 0

for i in range(n):
  matrix[i] = list(map(int, input()))

def dfs(y, x):
  if y-1 < 0 or x-1 < 0 or y+1 > n or x +1 > m: #정답지에 범위가 왜 저건지 모르겠다..
    return False
  if matrix[y][x] == 0:
    matrix[y][x] = 1
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)
    return True
  return False

for y in range(n):
  for x in range(m):
    if dfs(y, x) == True:
      result += 1

print(result)