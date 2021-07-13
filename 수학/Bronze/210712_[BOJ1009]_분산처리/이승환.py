# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     if a == 0:
#         print(10)
#     else:
#         result = a**b
#         print(result%10) 
# 시간초과
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    result = [(a ** i) % 10 for i in range(1,5)][(b % 4) -1]
    print(result if result != 0 else 10)
    # a = a % 10
    
    # if a == 0:
    #     print(10)
    # elif a == 1 or a == 5 or a == 6:
    #     print(a)
    # elif a == 4 or a == 9:
    #     b = b % 2
    #     if b == 1:
    #         print(a)
    #     else:
    #         print((a * a) % 10)
    # else:
    #     b = b % 4
    #     if b == 0:
    #         print((a**4) % 10)
    #     else:
    #         print((a**b) % 10)