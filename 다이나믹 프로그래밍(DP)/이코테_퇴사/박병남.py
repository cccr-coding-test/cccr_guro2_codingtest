N = int(input())
times = [list(map(int,input().split())) for i in range(N)]

dp = [0]*(N+1)

for i in range(N-1,-1,-1):
    time=times[i][0]+i
    if time > N:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(times[i][1]+dp[time],dp[i+1])

print(dp[0])
