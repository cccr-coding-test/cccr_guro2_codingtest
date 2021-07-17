while True:
    a=input()
    if a=='0':
        break
    result=len(a)+1
    for i in a:
        if i=='1':
            result+=2
        elif i=='0':
            result+=4
        else:
            result+=3
    print(result)

