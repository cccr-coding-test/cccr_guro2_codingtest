# 현재 나이트의 위치 입력
location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1

count= 0

#나이트가 이동할 수 있는 8가지 방향 정의
routes = [(1,2), (1,-2), (2,1), (2,-1) ,(-1,2), (-1,-2), (-2,1), (-2,2)]

# 8가지 방향에 대한 위치로 이동 가능한지 확인
for route in routes:
    # 나이트의 초기 위치에서 다음 위치 지정
    next_row = row + route[0]
    next_column = column + route[1]
    # 나이트의 위치가 8 X 8 안에 존재할 때 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <=8:
        count += 1

print(count)
