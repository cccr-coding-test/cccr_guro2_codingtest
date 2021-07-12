n=int(input())
mylist=list(map(int,input().split()))
y,m=0,0
for my in mylist:
    y+=(my//30+1)*10
    m+=(my//60+1)*15
if m==y:
    print('Y M',m)
else:
    print('M', m) if m<y else print('Y',y)
