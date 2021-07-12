import sys
input=sys.stdin.readline
for _ in range(3):
    testCase=int(input())
    mynum=0
    for _ in range(testCase):
        a=int(input())
        mynum+=a
    if not mynum:
        print(0)
    else:
        print('+') if mynum>0 else print('-')
