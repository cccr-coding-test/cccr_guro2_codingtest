N,M = map(int, input().split())
d = []

for _ in range(N):
    d.append(map(int, input().split()))

value = 0
for i in d:
    min_num = min(i)
    value = max(0,min_num)

print(value)
    

