cnt = int(input())

index = {1:0, 2:1, 3:2}

for i in range(cnt):
    a, b = map(int, input().split())
    index[a], index[b] = index[b], index[a]

for key, value in index.items():
    if value == 0:
        print(key)