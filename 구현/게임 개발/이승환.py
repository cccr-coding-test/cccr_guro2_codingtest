n, m = map(int, input().split())
x, y, direction = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

darray = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

darray[x][y] = 1
count = 1
turned_count = 0

while True:
    direction = direction - 1
    if direction == -1:
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]

    if darray[nx][ny] == 0 and array[nx][ny] == 0:
        darray[nx][ny] = 1
        count = count + 1
        x, y = nx, ny
        turned_count = 0
        continue

    else:
        turned_count = turned_count + 1

    if turned_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x, y = nx, ny
        
        else:
            break

        turned_count = 0

print(count)