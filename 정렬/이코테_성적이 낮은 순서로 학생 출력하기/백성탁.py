N = int(input())

d = []
for i in range(N):
    name_score = input().split()
    d.append((name_score[0], int(name_score[1])))

def order(data):
    return data[1]

result = sorted(d, key=order)

for name in result:
    print(name[0], end=' ')

    