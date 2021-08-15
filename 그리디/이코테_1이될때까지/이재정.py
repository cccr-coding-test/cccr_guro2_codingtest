N, K = map(int, input().split())

cnt = 0
while(True):
    if N == 1:
        print(cnt)
        break
    if K > 1 and N % K == 0:
        N /= K
        cnt += 1
    else:
        cnt += 1
        N -= 1