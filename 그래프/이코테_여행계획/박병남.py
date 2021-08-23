def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
goingto=list(set(map(int,input().split())))
parent=[i for i in range(n+1)]

for x in range(n):
    for y in range(x,n):
        if maps[x][y]==1:
            union_parent(parent,x+1,y+1)

myparent=find_parent(parent,goingto[0])
flag=True
for my in goingto:
    if myparent!=find_parent(parent,my):
        flag=False

print("YES") if flag else print("NO")
