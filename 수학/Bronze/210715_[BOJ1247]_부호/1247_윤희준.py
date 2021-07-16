import sys
r = []
for _ in range(3):
    N = int(sys.stdin.readline())
    s = 0
    for _ in range(N):
        n = int(sys.stdin.readline())
        s += n
    if s > 0:
        r.append('+')
    elif s < 0:
        r.append('-')
    else:
        r.append('0')
for i in r:
    print(i, end='\n')