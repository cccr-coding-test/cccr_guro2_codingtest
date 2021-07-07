import math
# c=대각선, a=높이, b=너비
c, a, b = map(int,input().split())
x = math.sqrt(c**2 / (a**2 + b**2))
print(int(a*x), int(b*x))