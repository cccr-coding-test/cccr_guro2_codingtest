n,m,k=map(int,input().split())
mylist=list(map(int,input().split()))
mylist.sort(reverse=True)
a=m//(k+1)
print(mylist[0]*(m-a)+mylist[1]*a)


