N = int(input())

d = []
for i in range(N):
    d.append(int(input()))

d.sort(reverse=True)

for i in d:
    print(i, end = ' ')
