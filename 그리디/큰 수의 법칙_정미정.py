# 그리디_큰 수의 법칙
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속 횟수 K
# 입력받은 수를 저장 a

n,m,k = map(int, input().split())
a = list(map(int, input().split())) # 리스트에 입력받기

a.sort() # 오름차순으로 정렬
last = a[n-1] # 가장 큰 수
second = a[n-2] # 두 번째로 큰 수

b = m//(k+1) # 가장 큰 수 last가 더해지는 횟수
print(last*(m-b)+second*b)
