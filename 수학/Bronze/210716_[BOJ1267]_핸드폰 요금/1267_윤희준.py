N = int(input())
n = list(map(int,input().split()))
Y = M = 0

for i in n:
    Y += i // 30 * 10 + 10
    M += i // 60 * 15 + 15

if Y < M:
    print("Y %d" % Y)
elif Y > M:
    print("M %d" % M)
else:
    print("Y M %d" % Y)