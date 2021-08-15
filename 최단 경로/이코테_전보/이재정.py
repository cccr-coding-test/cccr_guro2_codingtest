import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n + 1)]

distances = [INF] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
        curr_distance, curr_node = heapq.heappop(queue)
        if distances[curr_node] < curr_distance:
            continue
        for i in graph[curr_node]:
            distance = curr_distance + i[1]
            if distance < distances[i[0]]:
                distances[i[0]] = distance
                heapq.heappush(queue, (distance, i[0]))


dijkstra(c)

count = 0
time = 0
for i in range(1, n + 1):
    if distances[i] == INF:
        continue
    else:
        count += 1
        time = max(time, distances[i])

print(count - 1, time)