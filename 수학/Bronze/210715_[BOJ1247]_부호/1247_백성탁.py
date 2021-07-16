from sys import stdin

result = [ ]

for _ in range(3):
    n = int(stdin.readline())
    d = [ ]

    for i in range(n):
        d.append(int(stdin.readline()))

    S = sum(d)
    # S=0
    # for i in d:
    #     S += i
        
    if S < 0:
        result.append('-')
    elif S > 0:
        result.append('+')
    else:
        result.append(0)

for x in result:
    print(x)

