# N,M,K = map(int, input().split())
# d = []
# sum = 0

# for _ in range(N):
#     d.append(map(int,input().split()))


# sort 개념..체크.. 책 문제해설보고 다시 풀어보겠습니다..

# 주어진 배열에서 가장 큰 수를 K번까지 반복해서 더할 수 있는데
# 만약 K번 반복 후, 그 다음으로 배열에서 큰 수가 더해지고
# 다시 K번 반복하여 총 M의 수가 더하여 결과 도출..
# 같은 숫자라도 인덱스가 다르면 가능

#-----------------------------------------------------------------------------

# 배열의 크기 N | 숫자가 더해지는 횟수 N | 가장 큰 수가 더해지는 횟수 K
N,M,K = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[N -1] # 가장 큰 수
second = data[N -2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1 # 더할 때 마다 1씩 빼기
    if M == 0:
        break
    result += second
    M -= 1

print(result)


#-----------------------------------------------------------------------------

data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0

while M != 0:
    for i in range(K):
        result += first
        M -= 1

    result += second
    M -= 1

print(result)


#------------------------------------------------------------------------------
# 가장 큰 수가 더해지는 횟수
# 반복되는 수열
# 수열의 길이 K + 1 ---> M / (K+1) ==> 수열이 반복되는 횟수*K <가장 큰수가 등장하는 횟수)
# but 나누어 떨어지지 않을 때
# int(M/(K+1))*K + M%(K+1) 

# 병남
a=m//(k+1)
print(mylist[0]*(m-a)+mylist[1]*a)
# 미정
b = m//(k+1) 
print(last*(m-b)+second*b)


#재정
cycle_value = (K*arr[0])+arr[1]
result = int((( M/(K+1) )*cycle_value) + (( M % (K+1))*arr[0]))
#희준
result = (int(M/(K+1)) * (K*n1+n2) + (M%(K+1))*n1)


