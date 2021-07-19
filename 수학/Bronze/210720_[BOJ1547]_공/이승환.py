n = int(input())

cups = [1, 2, 3]

for i in range(n):
    x, y = map(int, input().split())
    cups[x-1], cups[y-1] = cups[y-1], cups[x-1]

print(cups[0])


# for i in range(n):
#     x, y = map(int, input().split())
#     xi = cups.index(x)
#     yi = cups.index(y)
    
#     cups[xi], cups[yi] = cups[yi], cups[xi]