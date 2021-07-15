import sys

 
for i in range(3):
    li=[]
    for j in range(int(sys.stdin.readline())):
        li.append( int(sys.stdin.readline()))
    if sum(li)>0:
        print("+")
    if sum(li) == 0:
        print("0")
    if sum(li) < 0:
        print("-")
