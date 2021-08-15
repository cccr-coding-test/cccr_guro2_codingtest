INF = int(1e9)  # 무한대 값으로 10억 설정

# 노드 개수 및 간선 개수 입력
n, m = map(int, input().split())
# 2차원 리스트 생성, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)

# 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 모든 간선 정보 입력 후 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    graph[a][b] = 1
    graph[b][a] = 정

# 거쳐 가는 노드 x와 최정 목적지 노드 K 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
distance = graph[1][k] + graph[k][x]

# 예외 처리
if distance >= 1e9:
    print("-1")
else:
    print(distance)