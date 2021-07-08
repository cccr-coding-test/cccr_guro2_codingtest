A, B, C = map(int, input().split())
if B < C:
    n = (A//(C-B))
    print(n +1)
else:
    print(-1)