# 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법

n = int(input())
n_set = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_set:
        print('yes', end=' ')
    else:
        print('no', end=' ')
