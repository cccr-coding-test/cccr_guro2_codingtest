n = int(input())
time = list(map(int,input().split()))

Y = 0
M = 0
for i in range(n):
    if time[i] < 30:
        Y += 10
    else:
        Y += (time[i]//30 +1)*10 

    if time[i] < 60:
        M += 15
    else:
        M += (time[i]//60 +1)*15 

if Y < M:
    print('Y', Y)
elif Y > M:
    print('M', M)
else:
    print('Y', "M", Y)
    




# y = 30초 마다 10원 -> 60초 마다 20원
# m = 60초 마다 15원