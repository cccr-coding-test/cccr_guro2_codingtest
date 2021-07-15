result = [ ]

for _ in range(3):
    n = int(input())
    d = [ ]

    for i in range(n):
        d.append(int(input()))

    S=0
    for i in d:
        S += i
        

    if S < 0:
        result.append('-')
    elif S > 0:
        result.append('+')
    else:
        result.append(0)

for x in result:
    print(x)

