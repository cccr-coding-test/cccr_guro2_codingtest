# 이진 탐색: 탐색 범위를 반으로 줄여나가면서 데이터를 빠르게 탐색
# 배열 내부의 데이터가 정렬되어 있을 때만 사용
# 3가지 변수 사용(시작점, 끝점, 중간점)
# 시작점, 끝점: 탐색하고자 하는 범위 / 중간점: 찾고자 하는 데이터와 비교
# 단순히 정렬된 배열에서 특정한 데이터를 찾도록 요구하는 문제 -> bisect 모듈 사용

from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
array = list(map(int, input().split()))

# left: 정렬된 array 리스트에서 x가 왼쪽에서 몇 번째 인덱스에 들어갈 수 있는지
# right: x를 삽입할 가장 오른쪽 인덱스
# array에서 값이 x인 원소 개수는 right - left
left = bisect_left(array, x)
right = bisect_right(array, x)

if right == left:
    print(-1)
else:
    print(right - left)
