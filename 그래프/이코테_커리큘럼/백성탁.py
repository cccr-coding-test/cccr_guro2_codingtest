# 위상 정렬... 풀이 참조...
# 공부 더 필요...

from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
gragh = [[] for i in range(v+1)]

time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] #첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        gragh[x].append(i)

#위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) #알고리즘 수행 결과를 담을 리스트
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in gragh[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()