while(True):
    N = input()
    if N == "0":
        break
    sum = 2
    for i in N:
        if i == "1":
            sum += 2
        elif i == "0":
            sum += 4
        else:
            sum += 3
        sum += 1
    sum -= 1
    print(sum)
