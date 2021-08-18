from bisect import bisect_left,bisect_right

n,x=map(int,input().split())
mylist=list(map(int,input().split()))
a=bisect_left(mylist,x)
b=bisect_right(mylist,x)
print(b-a) if a!=b else print(-1)
