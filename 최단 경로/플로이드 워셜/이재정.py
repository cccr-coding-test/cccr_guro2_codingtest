INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0  # 자기 자신으로 가는 비용은 0으로 초기화

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # a에서 b로 가는 비용과 a에서 k를 거쳐 b로 가는 비용을 비교
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()