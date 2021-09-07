def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

# 집의 수 n, 도로의 수 m
n,m=map(int,input().split())
#임의의 집 x,y 사이의 도로 길이 z
maps=[list(map(int,input().split())) for _ in range(m)]
maps.sort(key=lambda x: x[2])
total=0
parent=[i for i in range(n)]
for map in maps:
    x,y,cost=map
    if find_parent(parent,x)!=find_parent(parent,y):
        union_parent(parent,x,y)
    else:
        total+=cost

print(total)
