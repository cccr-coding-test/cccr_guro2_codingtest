import sys

#3개의 줄에 대한 테스트 케이스
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
