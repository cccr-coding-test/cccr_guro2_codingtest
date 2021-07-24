# 책 풀이 참조
# 이해가 어려운 부분이 많아 더 살펴보겠습니다...

N,M = map(int, input().split())

pack = []
for _ in range(N):
    pack.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False 

    if pack[x][y] == 0: 
        pack[x][y] = True
        dfs(x-1,y) 
        dfs(x+1,y) 
        dfs(x,y-1) 
        dfs(x,y+1) 
        return True
        
    if pack[x][y] == 1:
        return False


cnt = 0
for x in range(N):
    for y in range(M):
        if dfs(x, y) == True:
            cnt += 1

print(cnt) 