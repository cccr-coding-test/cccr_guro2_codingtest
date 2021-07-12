test_case = int(input())

for _ in range(test_case):
    a, b = map(int, input().split())
    a = a % 10
    
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)    ## a = 1,5,6일 때 자기 자신과 같은 똑같은 끝자리 수 출력
   
    elif a == 4 or a == 9:
        b = b % 2   ## 4일때 4,6  | 9일때 9,6
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4   ## 2,3,7,8 모두 끝자리 수 반복 주기가 4
        if b == 0:
            print((a ** 4 ) % 10 )
        else:
            print((a ** b) % 10)
