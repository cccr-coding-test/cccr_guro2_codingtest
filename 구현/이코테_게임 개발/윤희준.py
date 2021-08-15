# 세로(N), 가로(M)
N, M = map(int, input().split())
# 방문 위치 저장하기 위한 맵 생성하여 0으로 초기화..
visit = [[0] * M for _ in range(N)] 

# 캐릭터가 있는 좌표 (x,y), 바라보는 방향 d
x, y, d = map(int, input().split())
# 캐릭터 위치 방문처리
visit[x][y] = 1

# 맵 정보 입력 받기
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 왼쪽 방향 회전
def d_left():
    global d
    d -= 1
    if d == -1:
        d = 3
    
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 1
turn = 0

# 게임 시작
while True:
    d_left()
    nx = x + dx[d]
    ny = y + dy[d]
    # 회전 이후, 가보지 않은 칸 존재
    if visit[nx][ny] == 0 and board[nx][ny] == 0:
        visit[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn = 0
        continue
    # 회전 이후, 가본 칸 or 바다
    else:
        turn += 1
    
    # 4방향 다 바다 or 가본 칸
    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 이동
        if board[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤에 바다면 종료
        else:
            break
        turn = 0

print(count)

# 혼자 하다가 머리 터질 뻔해서 게임 시작 부분 책 참고..