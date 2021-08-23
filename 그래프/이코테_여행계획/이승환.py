# 서로소 집합 알고리즘: union-find 연산으로 구성
# 모든 노드는 자신이 속한 집합을 찾을 때 루트 노드를 재귀적으로 찾음

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀적으로 호출
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

# 여행지 수 n, 여행 계획에 속한 도시의 수 m
n, m = map(int, input().split())
parent = [0] * (n+1)  # 부모 테이블

# 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# union 연산 수행
for i in range(N):
    data = list(map, input().split())
    for j in range(n):
        if data[j] == 1:    # 여행지가 연결된 경우 union 연산 수행
            union_parent(parent, i+1, j+1)

# 여행 계획 입력
plan = list(map(int, input().split()))

result = True
# 여행 계획에 속하는 모든 노드가 서로 연결되어 있지 않으면 false
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

# 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지 확인
if result:
    print('YES')
else:
    print('No')