import sys

input = sys.stdin.readline

n=int(input())
mylist=list()
for _ in range(n):
    name,a,b,c=input().split()
    mylist.append([name,int(a),int(b),int(c)])
mylist.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
for my in mylist:
    print(my[0])
