n = input()

mid = len(n) // 2
pre, post = 0, 0

for i in range(mid):
    pre += int(n[i])
    post += int(n[mid + i])

if pre == post:
    print('LUCKY')    
else:
    print('READY')
