def solution(x,y):
    a,b=int(x[-1]), int(y)
    if a%10==0:
        return 10
    mylist=[[],
            [1],
            [6,2,4,8],
            [1,3,9,7],
            [6,4],
            [5],
            [6],
            [1,7,9,3],
            [6,8,4,2],
            [1,9]
            ]
    myNum=len(mylist[a])
    return mylist[a][b%myNum]

testCase=int(input())
for _ in range(testCase):
    a,b=input().split()
    print(solution(a,b))
