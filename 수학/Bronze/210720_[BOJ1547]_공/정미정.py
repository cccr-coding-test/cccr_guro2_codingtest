a = int(input())
# b = [1,2,3]
b = [0,1,2,3]

for i in range(a):
    left, right = map(int, input().split())
    b[left], b[right] = b[right], b[left]
    print(b)
    #b[left-1], b[right-1] = b[right-1], b[left-1]
    # python은 temp를 안써도 된다! 편하다..,

print(b.index(1))
