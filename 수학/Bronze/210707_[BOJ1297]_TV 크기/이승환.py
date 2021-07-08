r, x, y = map(int, input().split())
a = r/((x**2+y**2)**0.5)
print(int(a*x), end=" ")
print(int(a*y))