n = int(input())
result = map(int, input().split(" "))
y, m = 0, 0

for i in result:
    y += (i//30 + 1)
    m += (i//60 + 1)

y = y*10
m = m*15

if y > m:
    print("M", m)
elif y == m:
    print("Y M", y)
else:
    print("Y", y)