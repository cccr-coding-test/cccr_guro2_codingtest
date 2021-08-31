import sys

g = int(sys.stdin.readline()) #탑승구
p = int(sys.stdin.readline()) #비행기
plane = []                    #탑승구 정보

for _ in range(p):
    plane.append(int(sys.stdin.readline()))

def parent_find(x):
    if x == parent[x]:
        return x
    p = parent_find(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y

cnt = 0  
parent = {}
for i in range(g+1):
    parent[i] = i

for i in plane:
    x = parent_find(i)
    if x == 0:
        break
    union(x, x-1)
    cnt += 1

print(cnt)