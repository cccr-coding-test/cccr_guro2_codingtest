P, K= map(int,input().split())

d = []
for i in range(2, int(P ** 0.5) + 1): #math.sqrt() 대신 **0
    while(P > 1):
        if(P % i == 0):
            P //= i #정수형 나눗셈
            d.append(i)    
        else:
            break

if(P > 1): 
  d.append(P)

# 소수...소인수분해...
# 에라토스테네스의 체...
# 다음 스터디에서 알려주세요...