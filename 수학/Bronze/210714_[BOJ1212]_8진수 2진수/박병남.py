### solution 1

x = input()
result=str()
for i,a in enumerate(x):
    n=int(a)
    temp=str()
    while n:
        temp+=str(n%2)
        n//=2
    if i!=0:
        while len(temp)<3:
            temp+='0'
    result+=temp[::-1]
if x=='0':
    print(0)
else:
    print(result)
    

    
### solution 2

print(bin(int(input(),8))[2:])
