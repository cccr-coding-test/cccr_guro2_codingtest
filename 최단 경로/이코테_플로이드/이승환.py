# 플로이드 워셜: 모든 지점에서 다른 모든 지점까지의 최단 경로 계산
# 3중 반복문 사용
# for k in range(1, n+1):
#   for a in range(1, n+1):
#       for b in range(1, n+1):
#           adj[a][b] = min(adj[a][b], adj[a][k], adj[k][b])

# n개의 도시, m개의 버스
# 도시 A에서 B로 가는 데 필요한 비용의 최솟값

INF = int(1e9)

n = int(input())    # 노드
m = int(input())    # 간선

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 간선 정보를 받아 그래프 정보 입력
for a in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
       for b in range(1, n+1):
           graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우
        if graph[a][b] == INF:
            print("0", end=" ")
        # 도달할 수 있는 경우 거리 출력
        else:
            print(graph[a][b], end=" ")
    print()