# 위상정렬 : DAG(diirect acyclic graph)에 대해서만 수행
# 큐 사용을 위한 라이브러리
from collections import deque
import copy

# 노드 개수 입력
v = int(input())
# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 견결된 간선 정보를 담기 위한 2차원 리스트 선언
gragh = [[] for i in range(v+1)]

time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보 입력
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] #첫 번째 수는 시간 정보를 담음
    for x in data[1:-1]:
        indegree[i] += 1
        gragh[x].append(i)

#위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) #알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 라이브러리 사용

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐 에서 원소 꺼내기 - popleft()
        now = q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in gragh[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬 수행 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()