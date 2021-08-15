here = input()
a = ord(here[0])
b = int(here[1])

# 나이트가 이동할 수 있는 모든 경우의 수
move = [(2,1),(2,-1), (1, -2), (-1, -2), (-2,-1), (-2, 1), (-1, 2), (1,2)]

# 8방향에 대하여 각 위치로 이동이 가능한지 확인
cnt = 0
for x, y in move:
    mx, my = a + x, b + y
    if ord("a") <= mx <= ord("h") and 1 <= my <= 8:
        cnt += 1
print(cnt)

