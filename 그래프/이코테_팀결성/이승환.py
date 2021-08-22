# 크루스칼 알고리즘
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)   # 부모 테이블 초기화

# 부모 테이블상엣 부모를 자기 자신으로 초기화
for i in range(0, n+1):
    parent[i] = i

# 각 연산 확인
for i in range(m):
    oper,a,b = map(int, input().split())
    # union 연산
    if oper == 0:
        union_parent(parent, a, b)
    # find 연산
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('No')