# n x m 금광
# n x m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력

# array[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j] = 얻을 수 있는 금의 최댓값

t = int(input())

for t in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # dp 테이블 초기화
    dp = []
    index = 0

    for i in range(n):
        # array를 m개씩 나눠서 dp 테이블에 append
        dp.append(array[index : index+m])
        index += m

    # 다이나믹 프로그래밍 - bottom-up 방식
    for j in range(1, m):   # 열
        for i in range(n):  # 행
            # 왼쪽 위
            if i == 0:
                dp[i][j] += max(dp[i+1][j-1], dp[i][j-1])
            # 왼쪽 아래
            elif i == n-1:
                dp[i][j] += max(dp[i-1][j-1], dp[i][j-1])
            # 왼쪽
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

    result = 0

    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)