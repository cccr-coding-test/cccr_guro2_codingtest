N, M = map(int, input().split())

g = []
for i in range(N):
    g.append(list(map(int,input())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우 바로 종료
    if x<= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재 노드 노방문
    if g[x][y] == 0:
        # 노드 방문처리
        g[x][y] == 1
        # 상 하 좌 우 위치 모두 재귀적으로 호출
        dfs(x,-1,y)
        dfs(x,y,-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result =0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 dfs 수행
        if dfs(i,j) == True:
            result += 1

print(result)

# 책..참고..