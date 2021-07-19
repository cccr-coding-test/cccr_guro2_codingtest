from collections import deque

while True:
    mylist=deque(map(int,input().split()))
    a=mylist.popleft()
    if a==0:
        break
    result=1
    for _ in range(a):
        sp=mylist.popleft()
        cut=mylist.popleft()
        result=result*sp-cut
    print(result)
