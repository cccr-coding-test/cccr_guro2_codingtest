N, M = map(int, input().split())

roads = []
for i in range(M):
    a, b, cost = map(int, input().split())
    roads.append((cost, a, b))

roads.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (N+1) 

for i in range(1, N+1):
    parent[i] = i


result = 0
total = 0
for road in roads:
    cost, a, b = road
    total += cost
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(total - result)