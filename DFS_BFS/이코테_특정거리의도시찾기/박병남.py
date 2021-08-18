from collections import deque
import sys

input=sys.stdin.readline

def bfs(start,K):
    queue=deque()
    queue.append(start)
    results = []
    while queue:
        now=queue.popleft()
        visited[now]=True
        if weight[now] > K:
            break
        for next_node in graphs[now]:
            if not visited[next_node]:
                weight[next_node]=weight[now]+1
                visited[next_node]=True
                queue.append(next_node)
                if weight[next_node]==K:
                    results.append(next_node)
    results.sort()
    if results:
        for result in results:
            print(result)
    else:
        print(-1)



N, M, K, X = map(int,input().split())
graphs=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graphs[a].append(b)
visited=[False] * (N+1)
weight=[0]*(N+1)

bfs(X,K)
