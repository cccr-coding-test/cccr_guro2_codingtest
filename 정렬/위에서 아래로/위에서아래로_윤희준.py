N = int(input())
a = []
for i in range(N):
    a.append(int(input))
a = sorted(a, reverse=True)
for i in a:
    print(i, end=' ')