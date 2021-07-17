while True:
    n = input()
    if n == '0':
        break

    answer = len(n)-1+2
    for i in n:
        if i in '1':
            answer += 2
        elif i in '23456789':
            answer += 3
        elif i in '0':
            answer += 4

    print(answer)
