M = int(input())
default = [1,2,3]


for i in range(M):
    x, y = map(int, input().split())

    X = default.index(x)
    Y = default.index(y)

    default[X],default[Y] = default[Y],default[X]

print(default[0])

# swap  
# 리스트 값의 위치(index)를 반환하여 swap