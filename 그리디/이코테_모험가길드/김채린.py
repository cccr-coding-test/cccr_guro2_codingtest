n = int(input())
fear_list = list(map(int,input().split()))
fear_list.sort()

count = 0
need = fear_list[0]
get = 0

for i in fear_list:
    if need == get:
        need = get = 0
        count += 1
    need = i
    get += 1

print(count)
