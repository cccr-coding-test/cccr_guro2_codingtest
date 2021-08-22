from collections import deque
import copy

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
n = int(input())
costs = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
for i in range(1, n+1):
    cost = list(map(int, input().split()))
    costs[i] = cost[0]
    pres = cost[1:-1]
    for pre in pres:
        graph[pre].append(i)
        degree[i] += 1

def topology_sort():
    result = copy.deepcopy(costs)
    q = deque()

    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
    
    while q:
        curr = q.popleft()
        for i in graph[curr]:
            result[i] = max(result[i], result[curr] + costs[i])
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)
    
    for i in range(1, n+1):
        print(result[i])

topology_sort()




