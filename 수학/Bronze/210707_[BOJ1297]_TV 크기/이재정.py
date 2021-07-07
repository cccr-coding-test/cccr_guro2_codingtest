diag, height, width = map(int, input().split())

sum_square = (height**2) + (width**2)

width = ((diag**2)*(width**2))/sum_square
height = ((diag**2)*(height**2))/sum_square

print(int(height**0.5), int(width**0.5))