while True:
    n = input()
    if n == '0':
        break

    d = []
    s = str(n)
    for i in range(len(s)):
        d.append(s[i])
    
    length = 2 + (len(s)-1) # 기본 공백(앞,뒤 == 2) + 숫자 사이의 공백
    for i in d:
        if i == '1':
            length += 2
        elif i == '0':
            length += 4
        else:
            length += 3

    print(length)




