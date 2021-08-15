positon = input() #a1 이런 식으로 입력받음
col = int(positon[1])
row = int(ord(positon[0]))-96 # ord(a)=97

# 갈 수 있는 경우의 수, x좌표와 y 좌료 분리해도 됨
cases = [(-2,1), (-2,-1), (2,1), (2,-1), (1,-2), (-1,-2), (1,2), (-1,2)]
location = 0

for case in cases:
    nr = row + case[0]
    nc = col + case[1]

    if nr >= 1 and nr <= 8 and nc >=1 and nr <= 8:
        location += 1

print(location)