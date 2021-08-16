N = int(input())
d = list(map(int,input().split()))
d.sort()

cnt = 0
group = 0

for i in d:
    cnt += 1
    if cnt >= i:
        group += 1
        cnt = 0

print(group)

