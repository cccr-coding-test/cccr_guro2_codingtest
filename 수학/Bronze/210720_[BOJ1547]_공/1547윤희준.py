M = int(input())
cup = [1,2,3]
for _ in range(M):
    X, Y = map(int,input().split())
    x = cup.index(X)
    y = cup.index(Y)
    cup[x], cup[y] = cup[y], cup[x]
print(cup[0])