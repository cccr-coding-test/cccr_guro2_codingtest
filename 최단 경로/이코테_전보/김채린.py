# ㅠ,,,채린 별세개 두렵다
#일단 책,,코드,,

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    # X->Y비용= Z
    graph[x].append((y, z))

def dijkstra(start):
   q = []
   # 시작 노드로 가기 위한 최단 경로는 0=>큐에 삽입
   heapq.heappush(q, (0, start))
   distance[start] = 0
   while q: # 큐가 비어있지 않다면
        # 가장 최단 거리 노드
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 ㄱㄱ
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count -1 출력
print(count - 1, max_distance)


#ㅠ 오후에 책 말고 다시 해보기..