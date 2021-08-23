# DFS: 최대한 멀리 있는 노드를 우선으로 탐색, 스택 자료구조 이용
# BFS: 가까운 노드를 우선으로 탐색, 큐 방식 이용

# N개의 도시, M개의 단방향 도로, 도로의 거리는 1
# X 도시에서 출발, 최단 거리가 K인 모든 도시의 번호를 출력

# 플로이드 워셜은 메모리 초과로 BFS 사용

from collections import deque

INF = 1e9
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [-1] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])
visit[x]
while queue:
    v = queue.popleft()
    print(v)
    for i in graph[v]:
        if visit[i] == -1:
            queue.append(i)
            visit[i] = visit[v] + 1

count = 0
for i in range(1, n+1):
    if visit[i] == k:
        print(i)
        count += 1
if count == 0:
    print(-1)

## BFS 어렵다