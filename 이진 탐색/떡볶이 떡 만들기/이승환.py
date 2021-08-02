# 떡의 개수와 요청한 떡의 길이 입력
n, m = map(int, input().split())
# 떡의 개별 높이 정보 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점, 끝점 설정
start = 0
end = max(array) # 끝점: 떡의 높이 중 가장 긴 떡이 높이

# 이진 탐색
result = 0
while(start <= end):
    total = 0
    # 절단기 높이 설정
    mid = (start + end) // 2
    for x in array:
        # 떡을 잘랐을 때 떡의 양 계산(떡의 길이가 절단기 높이보다 클 때만)
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid-1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색) : m이상인 경우 높이값을 높혀서 덜 자르도록 함
    else:
        result = mid
        start = mid + 1

print(result)