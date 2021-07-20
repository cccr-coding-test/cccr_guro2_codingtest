N,M,K = map(int, input().split())
d = []
sum = 0

for _ in range(N):
    d.append(map(int,input().split()))


# sort 개념..체크.. 책 문제해설보고 다시 풀어보겠습니다..

# 주어진 배열에서 가장 큰 수를 K번까지 반복해서 더할 수 있는데
# 만약 K번 반복 후, 그 다음으로 배열에서 큰 수가 더해지고
# 다시 K번 반복하여 총 M의 수가 더하여 결과 도출..
# 같은 숫자라도 인덱스가 다르면 가능