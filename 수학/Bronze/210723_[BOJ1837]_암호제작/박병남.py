# 무지성 풀이

p,k=map(int,input().split())
k_list=[]
bad_pw=0
for i in range(2,k):
    if all((i%j) for j in range(2,int(i**0.5)+1)):
        k_list.append(i)
for i in k_list:
    if p%i==0:
        bad_pw=i
        break
if bad_pw:
    print('BAD',bad_pw)
else:
    print('GOOD')
    
