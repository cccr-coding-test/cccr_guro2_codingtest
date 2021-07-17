r = []
while True:
    n = input()
    if n == "0":
        break
    s = len(n)+1
    for i in n:
        if i == "0":
            s += 4
        elif i =="1":
            s += 2
        else:
            s += 3
    r.append(s)
for i in r:
    print(i, end='\n')