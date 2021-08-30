G = int(input())
P = int(input())
line = []
for _ in range(P):
    line.append(int(input()))

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

parent = [0] * (G+1) 

for i in range(1, G+1):
    parent[i] = i

cnt = 0
for i in line:
    gate = find_parent(parent, i)
    if gate == 0:
        break
    else:
        union_parent(parent, gate, gate-1)
        cnt += 1

print(cnt)
