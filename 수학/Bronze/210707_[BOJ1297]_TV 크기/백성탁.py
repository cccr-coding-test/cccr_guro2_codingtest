import math

c,a,b = map(int, input().split())

n = a**2 + b**2
d = math.sqrt(math.floor(n))

x = a*c/d
y = b*c/d

print(math.floor(x))
print(math.floor(y))