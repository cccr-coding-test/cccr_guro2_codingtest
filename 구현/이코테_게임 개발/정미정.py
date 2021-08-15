N, M = map(int, input().split())
A, B, d = map(int, input().split())

game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

game_map[A][B] = '1'
count = 1
dir_count = 0
while True:
    d -= 1
    if d < 0:
        d = 3

    nx = A + dx[d]
    ny = B + dy[d]

    if game_map[nx][ny] == 0:
        game_map[nx][ny] = '1'
        A, B = nx, ny
        count += 1
        dir_count = 0
        continue
    else:
        dir_count += 1

    if dir_count == 4:
        nx = A - dx[d]
        ny = B - dy[d]

        if game_map[nx][ny] == 0:
            A, B = nx, ny
        else:
            break
        dir_count = 0

print(count)

### 다시 확인
