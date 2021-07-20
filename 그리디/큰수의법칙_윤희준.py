N, M, K = map(int,input().split())
n = list(map(int,input().split()))

n.sort(reverse=True) # 내림차순 정렬
n1 = n[0] # 첫번째로 큰 값
n2 = n[1] # 두번째로 큰 값

# int(M/(K+1))*K + M%(K+1) 가장 큰 수가 더해지는 횟수
result = ( int(M/(K+1)) * (K*n1+n2) + (M%(K+1))*n1 )
print(result)