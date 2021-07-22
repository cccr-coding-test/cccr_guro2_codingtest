location = input()
side = int(location[1])
updown = int(location[0])

count= 0

#나이트가 갈수 있는 모든 방향
routes = [(1,2), (1,-2), (2,1), (2,-1) ,(-1,2), (-1,-2), (-2,1), (-2,2)]

for route in routes:
    #나이트의 초기 위치에서 다음 위치 지정
    next_side = side + route[1]
    next_updown = updown + route[0]
    #나이트의 위치가 정사각형 안에 존재할 때 카운트 증가
    if next_side >= 1 or next_side <= 8 or next_updown >=1 or next_updown <=8:
        count += 1

print(count)