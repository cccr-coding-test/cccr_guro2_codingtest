n, m = map(int, input().split())  # n 가진 돈, m 생명체의 수
print(n//m)     # 생명체 하나에게 할당되는 돈
print(n % m)      # 분배할 수 없는 돈
