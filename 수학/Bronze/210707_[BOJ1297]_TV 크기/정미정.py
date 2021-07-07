import math as m

diagonal, height, width = map(int, input().split()) # 대각선, 높이 비율, 너비 비율
rate = m.sqrt(diagonal**2 / (height**2 + width**2))
print(int(rate*height), int(rate*width))
