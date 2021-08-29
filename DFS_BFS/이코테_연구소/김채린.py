# 모든걸 쏟아..채린 뇌가 사망한 자리입니다...RIP
import copy
import itertools
from collections import deque


def bfs():
    # 바이러스 위치를 큐로..
    q = deque(virus)
    
    # 방문했는지 확인 테이블 0으로 만들기
    visited = []
    for x in range(N):
        visited.append([0]*M)

    # 큐가 없을때까지
    while q:
        row, col = q.popleft()
        # print('row= ',row,'  col= ',col)
        # 바이러스 위치 의 행.열
        #시작점이 바이러스 위치...
        # [[],[],[],[]]
        # [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]

        # row col 범위 row-1>=0 or N  음수 or N보다 크면 겉에ㅔ 벽이니까 굳이 안해도됨 temp_arr[row - 1][col] == 0 아까 벽 설치 했으니께...더하고 뺀 위치가..0이면 ..그 벽이아닌곳이겟쥬..?
        # 상
        if row - 1 >= 0 and temp_arr[row - 1][col] == 0 and visited[row - 1][col] == 0:
            visited[row - 1][col] = 1  #방문처리
            temp_arr[row - 1][col] = 2 #바이러스 위치의 위를 2로 바꾸고..
            q.append([row - 1, col])

        # 하
        if row + 1 < N and temp_arr[row + 1][col] == 0 and visited[row + 1][col] == 0:
            visited[row + 1][col] = 1
            temp_arr[row + 1][col] = 2
            q.append([row + 1, col])

        # 좌
        if col - 1 >= 0 and temp_arr[row][col - 1] == 0 and visited[row][col - 1] == 0:
            visited[row][col - 1] = 1
            temp_arr[row][col - 1] = 2
            q.append([row, col - 1])

        # 우
        if col + 1 < M and temp_arr[row][col + 1] == 0 and visited[row][col + 1] == 0:
            visited[row][col + 1] = 1
            temp_arr[row][col + 1] = 2
            q.append([row, col + 1])


#입력을 받고요...
N, M = map(int, input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int, input().split())))
print(arr)


#바이러스 위치 리스트
virus = []

# 벽을 세울 수 있는 곳 리스트
temp = []
for i in range(N):
    for j in range(M):

        # 벽 세울수있는곳
        if arr[i][j] == 0:
            temp.append([i, j])

        # 바이러스 위치
        elif arr[i][j] == 2:
            virus.append([i, j]) 

# 벽을 세울수있는곳 중에 3개 고르는 경우의 수
result = list(itertools.combinations(temp, 3))
# [
# ([1, 2], [1, 3], [2, 3]),
# ([1, 2], [1, 3], [2, 4]),
# ([1, 2], [2, 3], [2, 4]), 
#([1, 3], [2, 3], [2, 4])
# ]
# print('result=',result)

min_area = 0
# 후보 개수 만큼 진행
for k in range(len(result)):
    temp_arr = copy.deepcopy(arr)

    # temp_arr = arr 
    # [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]
    for i in range(3):
        temp_arr[result[k][i][0]][result[k][i][1]] = 1  # 벽 세우기
        # [
        # ([1, 2], [1, 3], [2, 3]),
        # ([1, 2], [1, 3], [2, 4]),
        # ([1, 2], [2, 3], [2, 4]), 
        #([1, 3], [2, 3], [2, 4])
        # ]

    # 바이러스 전파 시작
    bfs()
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            #안전영역 갯수...
            if temp_arr[i][j] == 0:
                cnt += 1
    # 최소값.
    min_area = max(min_area, cnt)
print(min_area)