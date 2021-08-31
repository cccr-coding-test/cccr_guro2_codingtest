## O(n^2) 풀이
## 시간초과 풀이
gates=[i for i in range(100001)]
g_cnt=int(input())
p_cnt=int(input())
p_list=[int(input()) for _ in range(p_cnt)]
result=0
flag=False

for plane in p_list:
    if flag:
        break 
    for i in range(plane,-1,-1):
        if gates[plane]==-1:
            continue
        elif gates[plane]==0:
            flag=True
            break
        else:
            gates[plane]=-1
            result+=1

print(result)

### 다른 풀이
## O(nlogn)풀이

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

g_cnt=int(input())
p_cnt=int(input())
p_list=[int(input()) for _ in range(p_cnt)]
gates=[i for i in range(100001)]
result=0

for plane in p_list:
    ok=find_parent(gates,plane)
    if ok==0:
        break
    else:
        union_parent(gates,ok,ok-1)
        result+=1

print(result)
