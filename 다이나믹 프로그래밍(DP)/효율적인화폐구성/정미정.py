n, m = map(int, input().split())

money_type=[]
for _ in range(n):
  money_type.append(int(input()))

dp = [10001]*(m+1)

dp[0]=0
for i in range(n):
  for j in range(money_type[i], m+1):

    if dp[j-money_type[i]] != 10001:
      dp[j] = min(dp[j], dp[j-money_type[i]]+1)

# 계산된 결과 출력
if dp[m] == 10001:
  print(-1)
else:
  print(dp[m])
  
 ### 다시 확인
