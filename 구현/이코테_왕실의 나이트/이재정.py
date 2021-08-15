point = input() 
y = int(point[1])
x = ord(point[0]) - 97 + 1
cnt = 0

direct = [
    [-2, -1], [-2, 1], [2, -1], [2, 1],
    [-1, -2], [1, -2], [-1, 2], [1, 2]
]

for d in direct:
    ny = y + d[1]
    nx = x + d[0]
    if ny < 1 or nx < 1 or ny > 8 or nx > 8:
        continue
    cnt += 1

print(cnt)