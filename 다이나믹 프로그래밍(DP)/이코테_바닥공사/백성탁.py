N= int(input())
d = [0]*1001

# N = 1, (2*1)
# N = 2, (2*1, 2*1) (1*2 1*2) (2*2)
# N = 3, (2*1, 2*1, 2*1) (2*1, 1*2, 1*2) (2*1 2*2)  (1*2, 1*2, 2*1) (2*2 2*1)

# Bottom Up
d[1] = 1
d[2] = 3
for i in range(3, N+1):
    d[i] = (d[i-1] + d[i-2]*2)%796796

print(d[N])

